receipt = int(input("Какова выручка Вашей фирмы:  "))
costs = int(input("Каковы расходы Вашей фирмы:  "))
rest = (receipt - costs)
if rest > 0:
    print("Ваша фирма прибыльна")
if rest < 0:
    print("Ваша фирма генерирует отрицательную прибыль")
