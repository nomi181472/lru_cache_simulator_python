import doubly_linklist as dll
import random


class memory:
    def __init__(self):
        self.ram = None
        self.block = None
        # c1=None
        # c2=None
       # c3=None
       # self.Ram=None
        # C1=dll.doubly()
        # C2=dll.doubly()
        # C3=dll.doubly()

    def set(self, a=0, b=0, c=0, d=0, block=0):
        self.ram = a
        self.Ram = dict()
        self.block = block

        for i in range(int(self.ram/self.block)):
            self.Ram[i] = dll.doubly(self.block)
            temp = dll.doubly(self.block)
            for j in range(self.block):
                temp.Queue(random.randrange(1, 100, 1))
            self.Ram[i] = temp
           # print("\nKey:", key)
            # value.display()
        for key, value in self.Ram.items():
            print("\nKey:", key)
            value.display()

        # self.c1=b
       # self.c2=c
        # self.c3=d


if __name__ == "__main__":
    lru = memory()
    ram_size = int(input("Enter Ram Size:"))
    block_size = int(input("\nEnter Block Size:"))
    lru.set(ram_size, 0, 0, 0, block_size)
