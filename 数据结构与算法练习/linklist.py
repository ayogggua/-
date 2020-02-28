# -*- coding=UTF-8 -*
class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None



class Singlelinklist(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        cur = self._head
        count = 0
        while cur:
            cur = cur.next
            count+=1
        return count

    def show(self):
        cur = self._head
        while cur:
            yield "value:"+str(cur.data)
            cur = cur.next
            if cur:
                yield "next:",cur.data
            else:
                yield "next",None

    def head_add(self,data):
        node = Node(data)
        node.next = self._head
        self._head = node #记得重新赋值头结点


    def tail_add(self,data):
        node = Node(data)
        if self.is_empty():
            self._head = node
        else:
            cur = self._head
            while cur.next:
                cur = cur.next


    def insert(self,data,index):
        if index <= 0:
            self.head_add(data)
        elif index >= self.length():
            self.tail_add(data)
        else:
            cur = self._head
            node = Node(data)
            for i in range(index-2):
                cur = cur.next
            node.next = cur.next
            cur.next = node

    def remove(self,data):
        cur = self._head
        pre = None
        while(cur.data!=data):
            pre = cur
            cur = cur.next
        if not pre:
            self._head = cur.next
        else:
            pre.next = cur.next
    
    def find(self,data):
        return data in self.show()



if __name__ == "__main__":
    linklist = Singlelinklist()
    for i in range(5):
        linklist.head_add(i)
    linklist.remove(4)
    # linklist.insert(99,4)
    print(linklist.find(9))
    print(list(linklist.show()))



