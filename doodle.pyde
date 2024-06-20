doodler = None
doodler_x, doodler_y = 0, 0
doodler_width, doodler_height = 50, 60
doodler_vy = 0
jump_speed = -15
gravity = 0.6
platforms = []
score = 0
move_speed = 3  # Скорость движения дудлика по горизонтали

def setup():
    size(400, 600)
    global doodler, doodler_x, doodler_y, doodler_width, doodler_height, jump_speed, gravity, platforms, score, doodler_vy
    doodler_x = width / 2 - doodler_width / 2
    doodler_y = height - doodler_height - 10
    doodler_vy = 0
    jump_speed = -15
    gravity = 0.6
    doodler = loadImage('doodle.png')  # Замените 'doodle.png' на путь к изображению персонажа
    platforms = [(width / 2 - 25, height - 10)]
    
    # Создаем начальные платформы
    for _ in range(10):
        platforms.append((random(width - 50), random(height)))


def draw_doodler():
    image(doodler, doodler_x, doodler_y, doodler_width, doodler_height)

def draw_platforms():
    fill(0, 255, 0)
    for platform in platforms:
        rect(platform[0], platform[1], 50, 10)

def check_platform_collision():
    global doodler_y, doodler_vy

    # Проверяем каждую платформу
    for platform in platforms:
        px, py = platform
        # Проверяем, если Doodler находится над платформой и может на нее прыгнуть
        if (doodler_x + doodler_width > px and
            doodler_x < px + 50 and
            doodler_y + doodler_height >= py and
            doodler_y + doodler_height <= py + 10 and
            doodler_vy > 0):
            doodler_vy = jump_speed
            break  # Прерываем проверку после первой найденной платформы
    
        
def generate_platforms():
    global platforms
    
    # Удаление платформ, которые вышли за пределы экрана
    platforms = [platform for platform in platforms if platform[1] < height]

    # Добавление новых платформ на расстоянии не больше 20 пикселей по вертикали
    while len(platforms) < 20:
        # Позиционирование новой платформы
        new_y = platforms[-1][1] - random(40, 50) if platforms else height - 10
        new_x = random(width - 50)
        
        platforms.append((new_x, new_y))


def display_score():
    fill(0)
    textSize(26)
    text("Score: " + str(score), 10, 30)
    
    
def draw():
    global doodler_x, doodler_y, doodler_vy, score
    background(255, 230, 234)
    draw_platforms()
    draw_doodler()
    doodler_y += doodler_vy
    doodler_vy += gravity

    # Двигаем платформы вниз, если Doodler поднимается выше середины экрана
    if doodler_y < height / 2:
        offset = height / 2 - doodler_y
        doodler_y = height / 2
        for i in range(len(platforms)):
            platforms[i] = (platforms[i][0], platforms[i][1] + offset)
        score += int(offset / 10)

    # Обработка столкновения с платформами
    check_platform_collision()
    # Генерация новых платформ
    generate_platforms()
    # Ограничение движения персонажа по горизонтали
    if doodler_x < 0:
        doodler_x = 0
    if doodler_x + doodler_width > width:
        doodler_x = width - doodler_width



    # Прыжок и движение влево/вправо при прыжке
    if doodler_vy != 0:
        if keyPressed and (keyCode == RIGHT or keyCode == ord('d')):
            doodler_x += move_speed
        if keyPressed and (keyCode == LEFT or keyCode == ord('a')):
            doodler_x -= move_speed

    display_score()
    
    # Проверка, достиг ли Doodler нижнего края экрана
    if doodler_y > height:
        game_over()

def game_over():
    background(255, 230, 234)
    fill(255, 0, 0)
    textSize(40)
    textAlign(CENTER)
    text("Game Over!", width / 2, height / 2)
    textSize(30)
    text("Score: " + str(score), width / 2, height / 2 + 40)
    noLoop()  # Останавливаем цикл draw(), чтобы игра больше не обновлялась
    
    
