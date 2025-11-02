def greet(name):
    print('hello, ' + name + '!')

greet('Iliyas')

def calculate_way(t, v):
    while True:
        if str(input('хотитке узнать путь? (да/нет) ')) == 'да':
            try:
                t = float(input('введите время (t): '))
                v = float(input('ведите скорость (v): '))
                s = t * v
                print('путь (s) равен: ' + str(s))
            except ValueError:
                print('пожалуйста, введите числовые значения для времени и скорости.')
        else:
            print('ок, до свидания!')
            break
calculate_way('программа запущена', 'ожидание ввода')


