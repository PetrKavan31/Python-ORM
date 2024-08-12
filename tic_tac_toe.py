a = ['|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|']
b = ['|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|']
c = ['|',' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ','|']
d = ['+','-','-','-','+','-','-','-','+','-','-','-','+']

def plus_minus():
    for elem in d:
        print(elem, end='')
    print()

def line_1():
    for elem in a:
        print(elem, end='')
    print()

def line_2():
    for elem in b:
        print(elem, end='')
    print()

def line_3():
    for elem in c:
        print(elem, end='')
    print()

def rounds():
    plus_minus()
    line_1()
    plus_minus()
    line_2()
    plus_minus()
    line_3()
    plus_minus()

rounds()

count = 1
while count < 10:
    if count % 2 != 0:
        position_X = int(input('Player X turn. Enter the position (1-9): '))
        if position_X == 1:
            a[2] = 'X'
            count += 1
            rounds()
        elif position_X == 2:
            a[6] = 'X'
            count += 1
            rounds()
        elif position_X == 3:
            a[10] = 'X'
            count += 1
            rounds()
        elif position_X == 4:
            b[2] = 'X'
            count += 1
            rounds()
        elif position_X == 5:
            b[6] = 'X'
            count += 1
            rounds()
        elif position_X == 6:
            b[10] = 'X'
            count += 1
            rounds()
        elif position_X == 7:
            c[2] = 'X'
            count += 1
            rounds()
        elif position_X == 8:
            c[6] = 'X'
            count += 1
            rounds()
        elif position_X == 9:
            c[10] = 'X'
            count += 1
            rounds()
        else:
            print('Wrong number')
    else:
        position_O = int(input('Player O turn. Enter the position (1-9): '))
        if position_O == 1:
            a[2] = 'O'
            count += 1
            rounds()
        elif position_O == 2:
            a[6] = 'O'
            count += 1
            rounds()
        elif position_O == 3:
            a[10] = 'O'
            count += 1
            rounds()
        elif position_O == 4:
            b[2] = 'O'
            count += 1
            rounds()
        elif position_O == 5:
            b[6] = 'O'
            count += 1
            rounds()
        elif position_O == 6:
            b[10] = 'O'
            count += 1
            rounds()
        elif position_O == 7:
            c[2] = 'O'
            count += 1
            rounds()
        elif position_O == 8:
            c[6] = 'O'
            count += 1
            rounds()
        elif position_O == 9:
            c[10] = 'O'
            count += 1
            rounds()
        else:
            print('Wrong number')
print("End of Game")