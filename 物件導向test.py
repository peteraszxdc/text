import random

class Die:
    def __init__(self):
        self.value = 0

    def roll(self):
        self.value = random.randint(1, 6)
class DiceGame:
    def __init__(self):
        self.dice = [Die() for _ in range(4)]

    def roll_all_dice(self):
        for die in self.dice:
            die.roll()

    def get_dice_values(self):
        return [die.value for die in self.dice]

    def play(self):
        while True:
            input("按Enter键摇骰子...")
            self.roll_all_dice()
            values = self.get_dice_values()
            print("摇出的点数:", values)
            if self.is_xi_ba_dou_zai(values):
                print("喜八豆仔！恭喜你赢了！")
                break
            else:
                print("再来一次！")

    def is_xi_ba_dou_zai(self, values):
        # 喜八豆仔的规则是四颗骰子点数相同
        return len(set(values)) == 1

if __name__ == "__main__":
    game = DiceGame()
    print("欢迎来玩喜八豆仔游戏！")
    game.play()