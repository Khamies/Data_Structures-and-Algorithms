import time


class Node:
    key = None
    next = None
    previous= None


class DoubleLinkedList:

    head = None
    tail = None

    def push_front(self,key):

        new_node=Node()
        new_node.key=key
        new_node.next= self.head

        self.head=new_node

        if self.tail==None:
            self.tail=self.head


        return "Push front is Done"



    def pop_front(self):

        self.head = self.head.next

        return "Pop front is Done"



    def top_front(self):

        if self.head==None:
            print(" List is empty")
        else:
            print(self.head.key)


    def push_back(self,key):

        new_node=Node()
        new_node.key=key
        new_node.next= None
        new_node.previous=self.tail


        if self.tail!=None:
            self.tail.next= new_node

        self.tail= new_node

        if self.head==None:
            self.head = self.tail

        return "Push Back is Done"

    def pop_back(self):          # O(n)

        start=time.time()

        self.tail.previous.next=None
        self.tail=self.tail.previous

        end=time.time()

        print(" Time of Pop Back operation is: ", end-start)


        return " Pop back is Done"

    def top_back(self):

        if self.tail==None:
            print("List is empty")
        else:
            print(self.tail.key)








link_list=DoubleLinkedList()

link_list.push_front(10)

for i in range(1000000):
    link_list.push_back(i)



# link_list.top_back()
# link_list.pop_front()
# link_list.top_front()
link_list.pop_back()

link_list.top_back()
