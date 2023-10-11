from task_1 import List

def menu():
    print("МЕНЮ праграмы:\n"
          "1. 5 метадаў для работы са спісамі ў класе")

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

    match(var):
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

                match (n):
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