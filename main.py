def show_menu():
    print("1. Citire date")
    print("2. Determinare cea mai lunga subsecventa cu proprietatea ca toate numerele sale sunt pare")
    print(
        "3. Determinare cea mai lunga subsecventa cu proprietatea ca toate numerele sale sunt formate din cifre prime")
    print(
        "4. Determinare cea mai lunga subsecventa cu proprietatea ca toate numerele sale sunt palindroame")
    print("x. Exit")


def read_list():
    lst = []
    lst_str = input("Introduceti numerele listei separate prin cate un spatiu: ")
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst


def get_longest_all_even(lst):
    """
    Determina cea mai lunga subsecventa in care toate numerele sunt pare
    Input:
    Lista de numere intregi in care se cauta subsecventa
    Output:
    Cea mai lunga subsecventa care satisface proprietatea data
    """
    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_even = True
            for num in lst[st:dr + 1]:
                if num % 2 != 0:
                    all_even = False
                    break
            if all_even:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result


def test_get_longest_all_even():
    assert get_longest_all_even([2, 6, 7, 8, 10, 12, 14, 31]) == [8, 10, 12, 14]
    assert get_longest_all_even([11, 13, 27, 53, 409]) == []
    assert get_longest_all_even([22, 24, 25, 26, 28, 30, 32, 34]) == [26, 28, 30, 32, 34]


def has_all_prime_digits(n):
    """
    Determina daca un numar dat contine doar cifre prime
    Input:
    n, numar intreg
    Output:
    True, n are doar cifre prime
    False, n nu are doar cifre prime
    """
    while n != 0:
        if n % 10 != 2 and n % 10 != 3 and n % 10 != 5 and n % 10 != 7:
            return False
        n = n // 10
    return True


def test_has_all_prime_digits():
    assert has_all_prime_digits(273) == True
    assert has_all_prime_digits(364) == False
    assert has_all_prime_digits(37275) == True


def get_longest_prime_digits(lst):
    """
    Determina cea mai lunga subsecventa in care toate numerele sale au doar cifre prime
    Input:
    Lista de numere intregi in care se cauta subsecventa
    Output:
    Cea mai lunga subsecventa care satisface proprietatea data
    """
    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_prime_digits = True
            for num in lst[st:dr + 1]:
                if has_all_prime_digits(num) == False:
                    all_prime_digits = False
                    break
            if all_prime_digits:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result


def test_get_longest_prime_digits():
    assert get_longest_prime_digits([6, 2, 8, 2, 3, 5, 1, 27]) == [2, 3, 5]
    assert get_longest_prime_digits([11, 12, 13, 14, 15]) == []
    assert get_longest_prime_digits([4, 6, 23, 7, 8, 22, 23, 25, 27]) == [22, 23, 25, 27]


def is_palindrome(n):
    '''
    Determina daca un numar este palindrom(numar care scris invers este egal cu el insusi) sau nu
    Input:
    n, numar intreg, n >= 0
    Output:
    True, n palindrom
    False, n nepalindrom
    '''

    copie = n
    oglindit = 0
    while n != 0:
        oglindit = oglindit * 10 + n % 10
        n = n // 10
    if (copie == oglindit):
        return True
    return False


def test_is_palindrome():
    assert is_palindrome(202) == True
    assert is_palindrome(23) == False
    assert is_palindrome(100) == False
    assert is_palindrome(7637) == False
    assert is_palindrome(1) == True


def get_longest_all_palindromes(lst):
    """
    Determina cea mai lunga subsecventa in care toate numerele sale sunt palindroame
    Input:
    Lista de numere intregi in care se cauta subsecventa
    Output:
    Cea mai lunga subsecventa care satisface proprietatea data
    """
    n = len(lst)
    result = []
    for st in range(n):
        for dr in range(st, n):
            all_palindromes = True
            for num in lst[st:dr + 1]:
                if is_palindrome(num) == False:
                    all_palindromes = False
                    break
            if all_palindromes:
                if dr - st + 1 > len(result):
                    result = lst[st:dr + 1]
    return result


def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([272, 393, 2, 4, 27]) == [272, 393, 2, 4]
    assert get_longest_all_palindromes([21, 23, 24, 25, 26, 27]) == []
    assert get_longest_all_palindromes([11]) == [11]
    assert get_longest_all_palindromes([2, 7, 90, 22, 44, 55, 16]) == [22, 44, 55]


def main():
    lst = []
    while True:
        show_menu()
        opt = input('Optiunea: ')
        if opt == '1':
            lst = read_list()
        elif opt == '2':
            all_even = get_longest_all_even(lst)
            if len(all_even) != 0:
                print("Cea mai lunga subsecventa cu toate numerele pare: ", all_even)
            else:
                print("Lista data nu contine numere pare")
        elif opt == '3':
            all_prime_digits = get_longest_prime_digits(lst)
            if len(all_prime_digits) != 0:
                print("Cea mai lunga subsecventa cu toate numerele compuse din cifre prime: ",
                      all_prime_digits)
            else:
                print("Lista data nu contine numere care sa fie compuse din cifre prime")
        elif opt == '4':
            all_palindromes = get_longest_all_palindromes(lst)
            if len(all_palindromes) != 0:
                print("Cea mai lunga subsecventa cu toate numerele palindroame: ",
                      all_palindromes)
            else:
                print("Lista data nu contine numere care sa fie palindroame")
        elif opt == 'x':
            break
        else:
            print('Optiune invalida')


if __name__ == '__main__':
    test_get_longest_all_even()
    test_has_all_prime_digits()
    test_get_longest_prime_digits()
    test_is_palindrome()
    test_get_longest_all_palindromes()
    main()
