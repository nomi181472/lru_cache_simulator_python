import doubly_linklist as dll
import random
import os


class memory:
    def __init__(self):
        self.ram = None
        self.block = None
        self.execution_list = list()
        self.execution_list_with_blocks = list()
        self.c1 = None
        self.c2 = None
        self.order1=None
        self.order2=None
        self.Level1 = None
        self.level2 = None
        self.MissPlanty=0
        self.hit_time=0
    def set(self, a=0, b=0, c=0, block=0):
        self.ram = a
        self.Ram = dict()
        self.block = block

        for i in range(int(self.ram/self.block)):
            self.Ram[i] = dll.doubly(self.block)
            temp = dll.doubly(self.block)
            for j in range(self.block):
                temp.Queue(random.randrange(1, 100, 1))
            self.Ram[i] = temp
            self.c1 = b
            self.c2 = c

    def Display(self):
        for key, value in self.Ram.items():
            print("\nBlock :", key)
            value.display(key, self.block)

    def execute_inst(self):
        while(1):
            self.Display()
            print("Instructions:", self.execution_list)
            print("blocks:", self.execution_list_with_blocks)
            print("press B: exit Selection\n")
            op = input("select instruction for execution:")
            if op == 'b'or op.lower() == 'b':
                break
            myblock = int(input("\nEnter Block number:"))

            self.execution_list.append(int(op))
            self.execution_list_with_blocks.append(myblock)
            os.system("cls")
    def Handle_cache1(self,bk,inst):
        if self.Level1 is None:
            self.Level1=dict()
            self.order1=dll.doubly(self.block)
        length_of_cache=len(self.Level1)
        if length_of_cache<(self.c1/self.block):
            value=self.Ram[bk]
            self.Level1[bk]=value
            self.maintain(bk,inst,True)

    def maintain(self,bk,inst,check):
        value=self.Level1[bk]
        self.hit_time=self.hit_time+1
        is_found,mi=value.findBlock(inst,check)
        self.MissPlanty=self.MissPlanty+mi
        if self.order1.counter!=-1 and check==False and is_found==True :
            self.order1.delete_node(bk)
            self.order1.Queue(bk)
        else:
            self.order1.Queue(bk)
        if is_found==False:
            self.execution_list.append(inst)
            self.execution_list_with_blocks.append(bk)     

    def start_execute(self):
        n=len((self.execution_list))
        for i in range(n):
            if  not(len(self.execution_list)==0):
                inst=self.execution_list.pop(0)
                bk=self.execution_list_with_blocks.pop(0)
                if self.Level1 is None or not(bk in self.Level1):
                    self.Handle_cache1(bk,inst)
                elif bk in self.Level1:
                    self.maintain(bk,inst,False)
                
                
                
                
                
                

            
        




if __name__ == "__main__":

    lru = memory()
    ram_size = int(input("Enter Ram Size:"))
    block_size = int(input("\nEnter Block Size:"))
    cache1_size = int(input("\nEnter Cache 1 Size:"))
    cache2_size = int(input("\nEnter Cache 2 Size:"))
    lru.set(ram_size, cache1_size, cache2_size, block_size)
    lru.execute_inst()
    lru.start_execute()
