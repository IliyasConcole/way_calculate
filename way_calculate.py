while True:
    if input('nachat? (y/n)')=='y':
        print('nachat')
        try:
                t = float(input('vvedite vrema: '))
                v = float(input('vvedite skorost km/m: '))
                s = v * t
                print('pyt', s)
        except ValueError:
                print('nepravilnoe znachenie')
    else:  
        print('poka')
        break