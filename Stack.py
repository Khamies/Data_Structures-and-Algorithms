
class Stack:

    def __init__(self, capacity):

        self.array=[]
        self.capacity=capacity
        self.pointer=-1

    def push(self,element):

        if self.pointer >= self.capacity:
            print(" Stack is full")
            return -1
        else:
            self.array.append(element)
            self.pointer+=1

            print("{} has been pushed".format(element))

            return 0


    def pop(self):
        if self.pointer==-1:
            print(" Stack is empty")
            return -1
        else:
            self.pointer-=1
            print("{} has been poped".format(self.array[self.pointer+1]))
            return 0


    def top(self):
        if self.pointer==-1:
            print(" Stack is empty")
            return -1

    def empty(self):
        if self.pointer==-1:
            print(True)
        else:
            print(False)


mstack=Stack(5)

mstack.push(10)
mstack.push(20)
mstack.top()
mstack.push(243)
mstack.push(11)
mstack.push(33)
mstack.push(35)
mstack.pop()
mstack.top()
mstack.empty()
mstack.pop()
mstack.pop()
mstack.pop()
mstack.pop()
mstack.pop()
mstack.top()