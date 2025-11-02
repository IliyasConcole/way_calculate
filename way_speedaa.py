while True:
    if input("Расчитать ускорение ? : (n/y)") == 'y':
        print("Расчет ускорения")
        try:
            t = float(input("введите время в секундах:"))
            v0 = float(input("введите изначальную скорость в м/с:"))
            a = float(input("Введите ускорение в м/с²:"))
            s = (v0 + t ) + ((a * t**2)/2) / 2
            print("Расстояние:", s)
        except ValueError:
            print("Неправильное значение")
    else:
        print("Пока")
        break