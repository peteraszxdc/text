import random

class Player:
    def __init__(self,name:str,dice=int):
        self.__nam = name
        self.dice = [dice() for _ in range(4)]

    @property
    def play():
        while(True):
            a=[random.randint(1, 6) for _ in range(4)]
            double=triple=quad=None
            for num in a:
                if a.count(num) == 2:
                    double = num
                elif a.count(num) == 3:
                    triple = num
                elif a.count(num) == 4:
                    quad = num
                else:
                    return

    def name(self) -> str:
        return self.__name
    def value(self) -> int:
        #呼叫self.__play()
        pass

    def __repr__(self) -> str:
        descript = ""
        descript += "徐國堂\n"
        descript += "骰子1=5\n"
        descript += "骰子2=3\n"
        descript += "骰子3=5\n"
        descript += "骰子4=5\n"
        dsecript += "得分=15分"
        return descript
if __name__ == '__main__':
    p1=Player("")
    print(p1.value)
    print(p1)
    