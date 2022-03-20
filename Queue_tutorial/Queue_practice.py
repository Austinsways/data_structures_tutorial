"""
This class of queue creates a data structure in python that is a queue
"""

import queue


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


"""Implement a system to hold numbers for customers waiting at a call center"""
#Create the queue object
call_queue = Queue()

#add the following numbers to the queue

#208-866-7756

#208-898 6657

#208-987-6543


print(f"customers in line: {call_queue}") #this should print the three customers number
"""dequeue two numbers then show the queue"""


print(f"customers in line after removing two {call_queue}") #this should print one customer number

#check if the queue is empty


#deque the last item then check again.


print(f"remaining in queue: {len(call_queue)}") #this should print no numbers