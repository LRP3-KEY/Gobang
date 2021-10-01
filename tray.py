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

    def fill_chess(self,chess):
        val=input("请开始输入行/列的数值(,):")
        value = val.split(",")


    def move_down(self,index,chess):
        if self.value not in self.movable_list:
            print("%d这里不能下棋子"%self.value)
            return

    def keep_vlue(self,value):
        keep = [] #收集数据
        keep.append(value)
        for i in keep:     #是否有连续五个数值





    #def is_win(self,chess):
        #pass



if __name__ == '__main__':
    pass

