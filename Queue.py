
class Queue:

    def __init__(self, capacity):

        self.capacity=capacity
        self.array=[]
        self.write=-1
        self.read=-1

    def enqueue(self,element):

        if self.read == -1 and self.write >= self.capacity:
            print(" Queue is empty")

            return -1

        else:
            self.array.append(element)
            self.write+=1
            print("{} has been pushed".format(element))

            return 0

    def dequeue(self):

        if self.read == self.write:
            print("Queue is empty")

            return -1
        else:
            self.read+=1
            print("{} has been removed".format(self.array[self.read-1]))

            return 0

    def top(self):

        if self.read == self.write:
            print(" Queue is empty")
            return -1

        else:
            print("++++++++++++++++++",self.array[self.write])
            return 0



    def empty(self):

        if self.read == self.write:
            print(True)
            return -1
        else:
            print(False)
        return 0



mqueue=Queue(5)

mqueue.enqueue(32)
mqueue.enqueue(43)
mqueue.enqueue(77)

mqueue.top()

mqueue.dequeue()
mqueue.dequeue()

mqueue.top()

mqueue.dequeue()
mqueue.top()
mqueue.dequeue()
mqueue.top()
