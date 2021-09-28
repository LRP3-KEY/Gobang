import tray

class Player():
    def __init__(self,name):
        self.name = name
        self.score = 0
        self.chess = None


    def move(self,chess_tray):
        index =-1
        while(index not in chess_tray.movable_list):
            try:
                index = int(input("请输入%s选择下棋的位置%s"%(self.name,chess_tray.movable_list)))
            except ValueError:
                pass
        chess_tray.move_down(index,self.chess)











if __name__ == '__main__':
    chess_tray = tray.Tray()
    human = Player("玩家一")
    human.chess = 0



