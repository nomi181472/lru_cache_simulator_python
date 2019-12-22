

class my_node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class doubly:
    def __init__(self,max):
        self.head = None
        self.counter = -1
        self.top = max

    def append(self, data):
        if self.head is None and self.counter < self.top:
            my_new_node = my_node(data)
            self.head = my_new_node
            self.counter = self.counter+1

        elif self.counter < self.top:
            my_new_node = my_node(data)
            my_new_node.next = self.head
            self.head.prev = my_new_node
            my_new_node.prev = None
            self.head = my_new_node
            self.counter = self.counter+1        
        else:
            print("Cache full")

    def at_direct_index(self, index, data):
        if(self.counter <= index):
            self.append(data)
            return
        my_new_node = my_node(data)
        if(index == 0):
            temp = self.head
            my_new_node.next = self.head
            self.head = my_new_node
            return

        curr = self.head
        i = 0
        while(i <= index-1):
            i = i+1
            curr = curr.next
        temp = curr.next
        curr.next = my_new_node
        my_new_node.prev = curr
        my_new_node.next = temp

    def Queue(self, data):
        if (self.counter==-1):
            self.append(data)
            return
        if (self.counter!=self.top-1):    
            my_new_node=my_node(data)
            my_new_node.next=self.head
            self.head=my_new_node
            self.counter=self.counter+1
        else:
            print("Cache iss full")
            
    def delete_node(self,data):
        cur=self.head
        if cur and cur.data==data:
            self.head=self.head.next
            cur=None
            self.counter=self.counter-1
            return
        prev=None
        while cur and cur.data!=data:
            prev=cur
            cur=cur.next
        if cur:
            prev.next=cur.next
            cur=None
            self.counter=self.counter-1
            return

        
        
    def display(self,mem=0,block=0):
        temp = self.head
        mem=mem*block
        while(temp):
            
            print(mem,': ',temp.data) 
            mem=mem+1
            temp = temp.next
    
    def Dequeue(self):
        cur = self.head

        if cur.next is None:
            cur = None
            self.head = None
        else:
            while (cur.next is not None):
                cur = cur.next

            prev = cur.prev
            prev.next = None
            cur.prev = None
            self.counter = self.counter-1
            return cur

    def findBlock(self,key,is_from_Ram):
        cur = self.head
        miss_planty=0
        while(cur):
            if is_from_Ram ==True:
                miss_planty=miss_planty+1
            if(cur.data == key):
                return tuple((True,miss_planty))
            cur = cur.next
        return(False,0)            

'''if __name__ == "__main__":
    obj=doubly(6)
    obj.Queue(3)
    obj.Queue(4)
    obj.Queue(5)
    obj.display()
    obj.delete_node(5)
    obj.display()
    obj.Queue(6)
    obj.display()
    obj.delete_node(3)
    obj.display()
    obj.Queue(1)
    obj.delete_node(6)
    obj.display()
'''
    

        