A linked list is a basic data structure that consists of nodes (sometimes called atoms), where ...

The most simple form of a linked list, a singly linked list consists of a node with data, and a pointer to the next node. For example : 

[diagram]()

Linked lists contain two special identifiers for the two special points in the list. A Head (or root) ... and a Null pointer for the tail. This lets us know where the front and the start of the linked list are.

There are a few basic operations that need to happen on a linked list.

You need to be able to add (place a new at the head of the list)
image
You need to be able to insert ( place a node in between two nodes)
image
You need to be able to get the value of the current node, and the next node
image
You need to be able to delete a node.
image


In python, linked lists are not included by default. However, Python (and many other languages) have a concept called [object oriented] programming, which allow for the implementation of our own data types. A sample implementation of a linked list is below:

Notice that you can only traverse 
The youtube channel computerphile has a great video on this.
[computerphilevideo()
