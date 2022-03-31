Queue

A queue is a data structure similar to a list. The queue takes item only from the front of the queue, and always adds items to the back of the queue. A queue has a first in first out mentality, every item waits its turn to be dequeued.
Queues are wonderful for holding fair and orderly lines.
Here's an example of a queues structure:
![Queue image](.\images\QueueStructure.jpeg)


A queue has the following methods:
    .enqueue(item) 
        this adds and item to the queue
        O(1) for adding items because it only ever adds to the back of the queue and moves no other items.
        Python representation: queue.append(item)
    .dequeue() 
        This removes an item from the front of the queue
        O(n) for removing an item because it always takes the item at the front of the queue, and moves the others forward
        Python representation: In python we need to save the value to a variable and then delete the variable from the list. 
            value = queue.pop[0]
    .size() 
        This return the length of the queue
        O(1) the length of the queue is stored as a variable and does not need to be cunted each time we call for it. 
        Python representation: length = len(queue)
    .empty() 
        This returns true if the queue is empty
        O(1) this checks if the size of the array is 0 and returns true if it is.
        Python representation: if len(queue == 0)

![Queue image](.\images\EnqueueExample.jpeg)

The example file shows an example of a queue

the practice file contains code to debug to show understanding of the queue data structure
    

