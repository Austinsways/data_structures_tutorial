"""
This class of queue creates a data structure in python that is a queue
"""

class Queue:
    """
    A basic implementation of a Queue
    """

    def __init__(self):
        """
        Start with an empty queue.
        """
        self.queue = []

    def enqueue(self, value):
        """
        Add an item to the queue
        """
        self.queue.append(value)
    def dequeue(self):
        """
        Remove the next item from the queue. 
        """
        value = self.queue[0]
        del self.queue[0]
        return value

    def is_empty(self):
        """
        Check to see if the queue is empty.
        """
        return len(self.queue) == 0
    
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """
        Provide a string representation for this object.
        """
        result = "["
        for item in self.queue:
            result += str(item)
            result += ", "
        result += "]"
        return result

"""
this is a line for a pizza restraunt, when a customer calls to order a pizza the name of the customer is added to the queue.
When we finish making the orders for the customers they are dequeued from the line. 
"""

#initializing the queue
pizza_line = Queue()
print(pizza_line)

#adding customers to the queue
pizza_line.enqueue("jim")
pizza_line.enqueue("Aly")
pizza_line.enqueue("Austin")
pizza_line.enqueue("jim") #notice jim is added twice for two different orders
pizza_line.enqueue("Bob")

#fulfilling customer orders

#printing the queue before removing orders
print("Pizza line before removing jim:")
print(pizza_line)

pizza_line.dequeue() #this dequeus the first customer in line, which is jim

print("Pizza line before removing jim:")
print(pizza_line)

#this checks if the queue is empty
if pizza_line.is_empty() == False:
    print("pizza line has customers waiting!")
else:
    print("pizza line is empty!")

#dequeue all the rest of the line.
pizza_line.dequeue()
pizza_line.dequeue()
pizza_line.dequeue()
pizza_line.dequeue()

#this shows the queue after its all dequeued
print("Pizza line after dequeing all:")
print(pizza_line)

if pizza_line.is_empty() == False:
    print("pizza line has customers waiting!")
else:
    print("pizza line is empty!")