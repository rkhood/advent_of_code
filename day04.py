def get_range(input_range='108457-562041'):
    val1, val2 = [int(i) for i in input_range.split('-')]
    return range(val1, val2 + 1)


def test_adjacent_digits(password):
    '''Two adjacent digits are the same (like 22 in 122345)'''
    num = str(password)

    x = num[0]
    for n in num[1:]:
        if n == x:
            return True
        else:
            x = n
    return False


def test_adjacent_double_digits(password):
    '''Two adjacent digits are the same (like 22 in 122345)'''
    num = str(password)

    test_digits = False
    x = num[0]
    counter = 1
    for n in num[1:]:
        if n == x:
            counter +=1
        else:
            if not counter % 2:
                test_digits = True
            if (counter > 1) and not (counter - 1) % 2:
                return False
            x = n
            counter = 1

    if not counter % 2:
        test_digits = True
    if not (counter - 1) % 2:
        return False
    return test_digits


def test_increasing(password):
    '''Going from left to right, the digits never decrease
    they only ever increase or stay the same (like 111123 or 135679)'''
    num = str(password)

    x = num[0]
    for n in num[1:]:
        if n >= x:
            x = n
        else:
            return False
    return True


if __name__ == '__main__':

    passwords = []
    for i in get_range():
        if test_adjacent_digits(i) and test_increasing(i):
            passwords.append(i)
    print(len(passwords))

    passwords = []
    for i in get_range():
        if test_adjacent_double_digits(i) and test_increasing(i):
            passwords.append(i)
    print(len(passwords))
