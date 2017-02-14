---
title: Abstract Data Types
---

# This page still under construction

The concept of an abstract data types introduces a few new concepts :

 - Abstraction : Abstraction is to omit or hide low-level details with a simpler, higher level idea.

 - Modularity : Dividing a system into individual components or modules, each of which can be seen as a seperate system and reused seperately from the original system
 
  - Encapsulation : Caputring a module inside it's own "capsule" so that it is responsible for everything it does, that other parts of the system cannot affect.
  
  - Information Hiding : Hiding details about how a module is implemented from the rest of the system, so that it can be changed and modified without changing the system (ie. the interface by which other parts of the program interact with is not changed)
  
   - Seperation of concerns : Similar to modularity, the concept of seperation means that each feature or "concern" is the responsibility of a single modlue, rather then repeating it across multiple modules.
 
Abstraction helps us in a pragmatic way by helping achieve ease of understanding, ease of debugging, and ease of change. It also helps us think about algorithms by leaving small implementation details out.

A Data type can be called abstract when it is defined by the operations that can occur on it, and when the implementation is hidden (underlying details are hidden) such that different implementations can replace an existing implementation without affecting how other programs interface with it.

A good checklist to use when determining if a data type is abstract is : 

- Does the data type define it's interface (how other programs talk to the data type) (sometimes known as a signature)
- Defines all known constants
- Defines a function in terms of the constants and composition with other functions
- The underlying details are hidden, so you don't know how the ADT does it's work, but you know what it does.

When we refer to functions here, we talk about a pure function, or mathematical function, where a function simply takes an input and returns an output, without affecting any other parts of the program (eg. global variables aren't changed)


Aside : 

The cartesian product**

When specifying an ADT, we use a specific type of notation, known as ______________

For example, with an append function on a graph :

addNode: Graph x node --> Graph
addEdge : Graph x edge --> Graph

By fully specifying every operation that can occur on an ADT, we can observe what each function will take in and return.

-- example --

