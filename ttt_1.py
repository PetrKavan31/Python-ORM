a = list('|   |   |   |')
b = list('|   |   |   |')
c = list('|   |   |   |')
d = list('+---+---+---+')

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
    p = 'X' if count % 2 != 0 else 'O'
    position_X = int(input(f'Player {p} turn. Enter the position (1-9): '))
    if position_X == 1:
        a[2] = p
        count += 1
        rounds()
    elif position_X == 2:
        a[6] = p
        count += 1
        rounds()
    elif position_X == 3:
        a[10] = p
        count += 1
        rounds()
    elif position_X == 4:
        b[2] = p
        count += 1
        rounds()
    elif position_X == 5:
        b[6] = p
        count += 1
        rounds()
    elif position_X == 6:
        b[10] = p
        count += 1
        rounds()
    elif position_X == 7:
        c[2] = p
        count += 1
        rounds()
    elif position_X == 8:
        c[6] = p
        count += 1
        rounds()
    elif position_X == 9:
        c[10] = p
        count += 1
        rounds()
    else:
        print('Wrong number')
print("End of Game")