class List:
    def __init__(self, lst):
        self.lst = [str(i) for i in lst]

    def add(self):
        print(f"Ваш спіс: {self.lst}.")
        el = input("Увядзіце элемент, які хочаце дадаць: ")

        self.lst.append(el)

    def delete(self):
        if self.lst == []:
            print("Спіс і так пусты, тут няма чаго выдаляць.")
        else:
            print(f"Ваш спіс: {self.lst}.")
            el = input("Увядзіце элемент, які хаце лі б прыбраць з спісу: ")

            if el in self.lst:
                self.lst.remove(el)
            else:
                print("Элемент не быў знойдзены ў спісе.")

    def lenght(self):
        print(f"Ваш спіс: {self.lst}.")
        print(f"Даўжыня спісу роўная: {len(self.lst)}.")

    def summ_int(self):
        print(f"Ваш спіс: {self.lst}.")

        sum_list = []
        for i in self.lst:
            if i.isdigit():
                sum_list.append(int(i))
            elif i[0] == '-' and i[1:].isdigit:
                sum_list.append(-1*int(i[1:]))

        sum1 = sum(sum_list)

        print(f"Сумма ўсіх цэлых лікаў з спісу роўна: {sum1}.")

    def clear(self):
        if self.lst == []:
            print("Спіс і так пусты, тут няма чаго ачышцаць.")
        else:
            self.lst = []
            print("Дадзеныя спісу былі ачышчаны. Цяпер спіс пусты.")