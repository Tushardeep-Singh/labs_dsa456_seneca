# Tushardeep Singh 160427217
```diff
Q1 : Please detail what exactly you did for the assignment.
A1 : I took on a leadership role in this assignment and was able to effectively distribute tasks among group members. 
     In part b, I defined constructor for Node, make_set, union_set, find_data, representative_node and representative functions.
     In Node constructor I made sure that default values were set to 'None' and that arguments were set to correct member variables. Also, I made sure that variable names made sense and were self explainatory.
     In make_set(), I made sure that both 'head' and 'tail' referred to new node, and that attributes next_node and prev_node were set to default values in new node.
     In union_set(), it was necessary that every node in other_set() pointed towards self and that 'tail' was correctly updated in union set. Also, other set 'head' and 'tail' was correctly updated after union.
     In find_data(), I made sure that correct reference to Node was returned.
     In representative_node(), I directly returned using get_front(), which directly returns self.head. The thing here is that, I don't have to check for a Node whose prev = None, because I made sure that once self.head was referred to first Node, it was never changed.
     In representative(), data was returned using get_data().
     
     In all of the assignment, I made sure to use the defined functions instead of always defining the logic, like using get_front() instead of using self.head .

     In part c, I defined make_set(), find_set(), union_set().
     In all of these functions I made sure to write code as clean as possible.

     I part d, my major contribution was towards comming up with logic on which our code will be based upon. Also, I came up with the idea of defining mark() and  equal_cell() to make code shorter and clean.

Q2 : What was one thing you learned when doing this assignment?
A2 : The one most important thing that I learned was, forming the logic before typing in the code. For eg in maze runner function if a person doesn't form logic of 
     how code must be made to work then it will be very difficult to continue writing the code once we start writing it down. 

Q3 : What was its most challenging aspect and what did you do to overcome this challenge?
A3 : The most challenging part was to assign correct size to set after union_set(). Actually, our code was assigning incorrect size after union_set(), if 2 sets 
     being combined contained one common element. 
     So, to overcome it I defined a logic wherein after combining the sizes of 2 combined sets(lets say A), next code block would find size of union set using iterative method (comparing parent of each element to root(lets say B)) and if B < A, then A = A - 1.
     A, if greater, will at most be greater by 1.
```