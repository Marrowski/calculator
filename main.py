while True:
    num_1 = int(input('Input number 1:'))
    num_2 = int(input('Input number 2:'))
    math_sign = input('Input math sign:')

    if math_sign == 'exit'.lower():
        break
    elif math_sign == '+':
        print(num_1 + num_2)
    elif math_sign == '-':
        print(num_1 - num_2)
    elif math_sign == '*':
        print(num_1 * num_2)
    elif math_sign == '/':
        if num_2 == 0:
            print('Sorry, but you cant divide on 0')
        else:
            print(num_1 / num_2)
    elif math_sign == '%':
        print(num_1 % num_2)
    elif math_sign == '**':
        print(num_1 ** num_2)
    else:
        print('Unknown action')
        continue
