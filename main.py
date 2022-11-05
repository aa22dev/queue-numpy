# importing numpy library
import numpy as np

# making a class for queue
class queue:
    def __init__(self, size): # constructor for defining the size of queue
        self.size = size # set size of queue
        self.elements = np.zeros([self.size], dtype='int8') # create a numpy array containing zeroes as initial value
        self.clear() # clear the queue by setting rear and front to -1 

    def enqueue(self, data): # enqueue function for adding value into queue
        if self.isFull(): # check whether the stack if full or not by checking position of rear variable
            print("Queue Overflow!") # if queue is full then print queue overflow
        else:
            self.rear = self.rear + 1 # change the position of rear to current value
            if self.front == -1: # if first value is being inserted
                self.front = 0; # then set front to 0
            self.elements[self.rear] = data # insert value into the queue

    def dequeue(self): # dequeue function for removing value from queue
        if self.isEmpty(): # check if stack is empty or not by checking position of rear variable
            return "Queue Underflow!" # print queue undeflow if queue is empty
        else:
            val = self.elements[self.front] # store first value of queue in variable 
            self.front = self.front + 1 # changing the position of front variable to point to next value available in queue
            return val # return the value

    def isEmpty(self):
        return ((self.front == -1 or self.rear == -1) or (self.front > self.rear)) # if front or rear variable have value -1 or value in front variable is greater than rear variable then return true

    def isFull(self):
        return (self.rear == self.size - 1) # if value of rear variable is equal to the total size of queue as defined by user then return true

    def frontV(self):
        return self.elements[self.front] # return first value of queue

    def rearV(self):
        return self.elements[self.rear] # return last value of queue

    def clear(self):
        self.rear = -1  # set rear to -1
        self.front = -1 # set front to -1

if __name__ == '__main__': # main function
    q = queue(3) # creating object of queue with size
    q.enqueue(5) # enqueing value in queue
    q.enqueue(6)
    q.enqueue(8)
    q.enqueue(9)
    print(q.dequeue()) # dequeing value from queue and printing it
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
