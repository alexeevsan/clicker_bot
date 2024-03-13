import pyautogui as bot
import time
import pyscreeze

# explorer "https://youtube.com"
# im1 = pyscreeze.screenshot()
# im2 = pyscreeze.screenshot('my_screenshot.png')

def bot_working():
    # открываем браузер по умолчанию
    time.sleep(0.5)
    bot.hotkey('win', 'r')
    bot.typewrite('explorer https://kliker-test.ru/')
    bot.press('enter')
    time.sleep(3)


    # устанавливаем время для теста
    x, y = pyscreeze.locateCenterOnScreen('./img/left.png')
    try:
        a, b = pyscreeze.locateCenterOnScreen('./img/right.png')
    except:
        a, b = pyscreeze.locateCenterOnScreen('./img/end.png')

    point = ((a - x) / 10)

    bot.moveTo(point * (case - 1) + x, b, duration=0.5)
    bot.click()


    # наводимся на кнопку старт
    x, y = pyscreeze.locateCenterOnScreen('./img/green.png')
    bot.moveTo(x, y, duration=0.5)


    # устанавливаем время для работы цикла
    max_time = int(cases[str(case)].split(' ')[0])
    start_time = time.time()


    # кликаем определенное время
    while (time.time() - start_time) < max_time:
        bot.click(x, y)

    time.sleep(1)


    # нажимаем кнопку ОК
    x, y = pyscreeze.locateCenterOnScreen('./img/ok.png')
    bot.moveTo(x+20, y, duration=0.5)
    bot.click()


cases = {
    '1': '1 секунда',
    '2': '2 секунды',
    '3': '5 секунд',
    '4': '10 секунд',
    '5': '15 секунд',
    '6': '30 секунд',
    '7': '60 секунд',
    '8': '100 секунд',
    '9': '120 секунд',
    '10': '300 секунд',
    '11': '1000 секунд',
}

print("Время работы бота: ")
for el in cases:
    print(f'{el}: {cases[el]}')


while True:
    case = input('\nВыберите время работы бота( 0 - выход ): ')

    if case == '0':
        break

    if case in cases:
        case = int(case)
        bot_working()
        break




