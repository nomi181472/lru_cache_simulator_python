

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
            curr = self.head
            while(curr.next):
                curr = curr.next
            curr.next = my_new_node
            my_new_node.prev = curr
            my_new_node.next = None
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
        self.append(data)

    def display(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def Dequeue(self):
        cur = self.head

        if cur.next is None:
            cur = None
            self.head = None
        else:
            while (cur.next is not None):
                cur = cur.next

            self.counter = self.counter-1
            prev = cur.prev
            prev.next = None
            cur.prev = None
            return cur