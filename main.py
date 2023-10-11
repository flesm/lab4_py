from task_1 import List
from task_2 import Alphabet, EngAlphabet


def menu():
    print("МЕНЮ праграмы:\n"
          "1. 5 метадаў для работы са спісамі ў класе. \n"
          "2. Заданне на стварэнне класу алфавіта.\n")

    while True:
        try:
            print("Увядзіце нумар задання: ")
            var = int(input())
            break
        except ValueError:
            print("Вы ўвялі не лік. Паспрабуце яшчэ раз")

    return var

while True:

    var = menu()

    match var:
        case 1:
            lst = ["apple", 15, 30, "amazon", "microsoft", 6, -234, "epam", 3, "tesla", "toyota", 931]
            list1 = List(lst)

            while True:
                print("Меню кіравання спісам:\n"
                      "1. Дадаць элемент у спіс.\n"
                      "2. Выдаліць элемент са спісу.\n"
                      "3. Палічыць даўжыню спісу.\n"
                      "4. Сумма цэлых значэнняў(улічваюцца і радковыя значэнні, яекія могуць быць пераведзены ў цэлае "
                      "значэнне).\n"
                      "5. Ачысціць спіс поўнасцю.\n"
                      "Любы іншы лік - Выхад з задання нумар 1.\n")

                while True:
                    try:
                        n = int(input("Увядзіце нумар метада спіса, які хочаце выклікаць: "))
                        break
                    except ValueError:
                        print("Вы ўвялі не лік. Паспрабуйце яшчэ раз.")

                match n:
                    case 1:
                        list1.add()
                    case 2:
                        list1.delete()
                    case 3:
                        list1.lenght()
                    case 4:
                        list1.summ_int()
                    case 5:
                        list1.clear()
                    case _:
                        break

        case 2:
            print("Выберыце адзін з варыянтаў: \n"
                  "1 - Прагляд работы бацькоўскага класа. \n"
                  "2 - Прагляд работы дачэрняга класа. \n")

            while True:
                try:
                    n = int(input("Варыянт №: "))
                    if n != 1 and n != 2:
                        raise Exception
                    break
                except ValueError:
                    print("Вы ўвялі не лік. Паспрабуйце яшчэ раз.")
                except Exception:
                    print("Значэнне можа быць роўным толькі 1 або 2.")

            if n == 1:
                while True:
                    try:
                        lang = input("Увядзіце мову (напрыклад 'EN' або 'BEL'): ")
                        for i in lang:
                            if i.isdigit():
                                raise Exception
                        break
                    except Exception:
                        print("Назва мовы не можа ўтрымліваць лічбы: ")

                while True:
                    try:
                        letters = input("Увядзіце літары алфавіта (праз прабел): ").split()
                        for i in letters:
                            if i.isdigit():
                                raise Exception("Алфавіт не можа ўтрымліваць лічбы.")
                            if len(i) != 1:
                                raise Exception("Даўжыня літары не павінна быць больш за 1")
                        break
                    except Exception as e:
                        print(e)

                alpha = Alphabet(lang, letters)
                while True:
                    print("Меню метадаў бацькоўскага класа:\n"
                          "1. Вывад літараў алфавіта.\n"
                          "2. Вывад даўжыні алфавіта.\n"
                          "Любы іншы - выхад у галоўнае меню.\n")

                    while True:
                        try:
                            m = int(input("Увядзіце нумар метада: "))
                            break
                        except ValueError:
                            print("Вы ўвялі не лік. Паспрабуйце яшчэ раз.")

                    match m:
                        case 1:
                            alpha.print()
                        case 2:
                            print(f"Памер алфавіту складае {alpha.letters_num()}")
                        case _:
                            break

            else:
                eng = EngAlphabet()

                while True:
                    print("Меню метадаў дачэрняга класа:\n"
                          "1. Праверка адносіны ўведзенай літары ў алфавіце.\n"
                          "2. Вывад даўжыні алфавіта.\n"
                          "3. Вывад сказу на англійскай мове.\n"
                          "Любы іншы - выхад у галоўнае меню.\n")

                    while True:
                        try:
                            m = int(input("Увядзіце нумар метада: "))
                            break
                        except ValueError:
                            print("Вы ўвялі не лік. Паспрабуйце яшчэ раз.")

                    match m:
                        case 1:
                            while True:
                                try:
                                    letter = input("Увядзіце адну літару англ. алфавіта: ")
                                    if letter.isdigit():
                                        raise ValueError("Увядзіце літару.")
                                    if len(letter) != 1:
                                        raise ValueError("Толькі адну.")
                                    break
                                except ValueError as e:
                                    print(e)

                            eng.is_en_letter(letter)
                            print()

                        case 2:
                            print(f"Даўжыня алфавіта складае: {eng.letters_num()} літар.\n")

                        case 3:
                            print("Вывад сказу на англійскай мове: ")
                            print(EngAlphabet.example(), end="\n")



