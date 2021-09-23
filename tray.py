class Tray(object):
    def __init__(self,col,line):
        self.col=col #col列
        self.line=line #line行
        self.tray_data=[[" "]*col]*line
        self.movable_list = list(zip(range(line),range(col)))


    def show_tray(self,show_index=False):
        for i in range(self.col):
            if show_index:
                for k in range(self.line):
                    print(" %s |" % (k) ,end = "")
                print("\n")

    def fill_chess(self,value):
        val=input("请开始输入行/列的数值(,):")
        value = val.split(",")


    def move_down(self,index,chess):
        if self.value not in self.movable_list:
            print("%d这里不能下棋子"%self.value)
            return










if __name__ == '__main__':
    k=Tray(10,10)
    k.show_tray(True)
    k.fill_chess()

