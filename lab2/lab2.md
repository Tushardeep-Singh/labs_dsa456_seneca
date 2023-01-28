# Lab 2
```diff
+ Author: Tushardeep Singh
+ Student Number: 160427217
```

```diff
+ Let 'number' be the input/parameter to function1(), wherein a series of calculations 
+ will be done using 'number' and a return value will be generated.
+ For analysis, let n = number. Then, loop will iterate 'n' number of times.
+ Let T(n) represent the total number of operations required to generate a return value,
+ where 'n' is the range of 'for' loop used below.
```
### function 1:

Analyze the following function with respect to number

```python
def function1(number):
	total=0;

	for i in range(0,number):
		x = (i+1)
		total+=(x*x)

	return total
```
```diff
+ explanation of count:

! total=0; # 1
+ Above, operator '=' will only be used once per function call and hence, has a count of 1.

! for i in range(0,number): # n + 1
+ Above, value of 'i' changes in every iteration of loop from 0 to (n-1). Thus, value of 'i'
+ changes n number of times, so count for 'i' is n.
+ range() gets called once per loop execution, to get values the loop must iterate through.
+ so, count = n+1

! x = (i+1) # 2n
+ Above, operators = and + ,each have a count of 1 and are called 'n' times.
+ so, count = 2n.

! total+=(x*x) # 2n
+ Above, operators += and *,each will be used n times and
+ operator count of += is 1,
+ so count = 2n.

! return total # 1
+ A value will be returned in every function call and a return will happen only once.
+ so, count = 1.



+ T(n):
+ Total number of operations required to generate a return value:
+ T(n) = (1) + (n+1) + (2n) + (2n) + 1
+ T(n) = 3 + 5n
+ T(n) = 5n + 3

+ We can also see that, 
+ 0 <= 5n + 3 <= 6n, where n >= 3
+ i.e 0 <= T(n) <= cf(n) is true for all n >= n`
+ Therefore, T(n) is O(n)

+ Above, T(n) is of the form (y = mx + c), at very large values of x, c will be insignificant
+ in comparison to mx. So, it will be a correct practice to remove 3 from T(n).
+ T(n) = 5n
+ Still, 0 <= 5n <= 6n, where n >= 0
+ It will be a correct practice to remove 5 because 0 <= n <= 6n ( 0 <= T(n) <= cf(n) ) where n >= 0
+ Therefore, T(n) is still O(n)

+ Hence, for n inputs, the maximum number of operations will be less than or equal to constant multiples of n.
+ It can also be written :
+ upper bound : O(n^2)
+ Lower bound : Ω(log n)

+ Short approach :
+ There are operators that run constant number of times, C1
+ There are operators that run 'n' number of times, C2*n
+ T(n) = C1 + (C2*n)
+ Removing all the constants and constant with leading order of growth.
+ T(n) = n
+ While doing asymptotic analysis we usually find the worst case, i.e. upper bound, so
+ 0 <= n <= 2n, where n >= 0
+ Hence, T(n) is O(n), for all n >= n`

+ We can also write,
+ upper bound : O(n^2)
+ lower bound : Ω(log n)
```



### function 2:

Analyze the following function with respect to number
```diff
+ Let 'number' be the input/parameter to function2(), wherein a series of calculations (BODMAS)
+ will be done using 'number' in return statement and a return value will be generated.
+ For analysis, let n = number.
+ Let T(n) represent the total number of operations required to generate a return value.

+ n(n+1)(2n+1)/6 where n >= 1
+ Above, statement is result of sum of square of integers where each integer >= 1. 
+ It will also get proved below when O(n) gets proved.
```
<!-- sum of square of integers is equal to n(n+1)(2n+1)/6 where n>= 1 -->

```python
def function2(number):
	return  ((number)*(number+1)*(2*number + 1))/6

```
```diff
+ explanation of count:

! return  ((number)*(number+1)*(2*number + 1))/6 # (1) + (1) + (1) + (1+1) + (1) + (1)
+ Above, when function2() gets called, return is used once, but there are 6 operations that occur
+ in return statement and each occurs once.
+ So, count = 6 + 1 = 7



+ T(n):
+ Total number of operations required to generate a return value:
+ T(n) = 7

+ We can also see that, 
+ 0 <= 7 <= 7n ,where n >= 1
+ i.e 0 <= T(n) <= cf(n) is true for all n >= n`
+ Therefore, T(n) is O(1) i.e. it has a constant order of growth.
+ Hence, the number of operations required will be constant as per the approach of the algorithm (in this case 7), irrespective of the input size.
```


### function 3:

<!-- this function orders the list in ascending order. -->
<!-- capital letters occur before lowercase letters -->

Analyze the following with respect to the length of the list. Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
```diff
+ Let 'list' be input/parameter to function3, wherein function orders the list in ascending order.
+ (capital letters occur before lowercase letters)
+ For analysis, let n = len(list)
+ Let T(n) represent the total number of operations required to arrange the list.

+ number of iterations in first 'for' loop : (n-1) : 0 to n-2 inclusive


+ Total number of iterations in second 'for' loop: n(n-1)/2
+ For analysis, let z = n(n-1)/2
! proof:
```
![proof](https://user-images.githubusercontent.com/113130891/213395372-309ebfec-2bdc-4d7f-8914-346ce0fbb2ce.jpeg)

```python

def function3(list):
	for i in range (0,len(list)-1):
		for j in range(0,len(list)-1-i):
			if(list[j]>list[j+1]):
				tmp=list[j]
				list[j]=list[j+1]
				list[j+1]=tmp

```
```diff
+ T(n):
+ Total number of operations required to order the list in ascending order:
```
![complete_calculation](https://user-images.githubusercontent.com/113130891/215256896-39bbf3c4-0438-479c-86b6-c85dacc6b55a.jpg)

```diff
+ Short approach:
+ Worst case:
+ Total number of operations in inside loop : n(n-1)/2 = (n^2)/2 - n/2
+ Removing all the lower orders of growth, constant values and constant with higher order of growth
+ T(n) = n^2
+ 0 <= n^2 <= 2(n^2), where n >= 0
+ Hence, T(n) is O(n^2), for all n >= n` i.e. for an input of size 'n', the maximum number of operations will be less than
+ or equal to a constant multiple of n^2

+ We can also write:
+ upper bound : O(n^3)
+ lower bound : Ω(log log n)
```
### function 4:


<!-- this function calculates factoral. -->

Analyze the following function with respect to number
```diff
+ Let 'number' be the input/parameter to function4 wherein function calculates the factoral of 'number'.
+ For analysis let n = number
+ Let T(n) be the total number of operations required to calculate factoral.

+ Number of iterations in for loop is (n-1) , 1 to (n-1) both inclusive.

```
```python
def function4(number):
	total=1 #1
	for i in range(1 to number): # (n-1) + 1
		total=total*(i+1) # 3(n-1)
	return total # 1
```

```diff
+ explanation of count:

! total=1 #1
+ Above, operator '=' will only be used once per function call and hence, has a count of 1.

! for i in range(1 to number): # (n-1) + 1
+ Above, value of 'i' changes in every iteration of loop from 1 to (n-1), both inclusive. Thus, value of 'i'
+ changes (n-1) number of times, so count for 'i' is (n-1).
+ range() gets called once per loop execution, to get values the loop must iterate through.
+ so, count = n

! total=total*(i+1) # 3(n-1)
+ Above, operators '=','*','+' are used in every iteration of the loop.
+ so, count = 3(n-1)

! return total # 1
+ A value will be returned in every function call and a return will happen only once.
+ so, count = 1.

+ T(n):
+ Total number of operations required to generate a return value:
+ T(n) = 1 + n + 3n - 3 + 1
+ T(n) = 4n - 1

+ We can also see that, 
+ 0 <= 4n - 1 <= 5n, where n >= 1
+ i.e 0 <= T(n) <= cf(n) is true for all n >= n`
+ Therefore, T(n) is O(n)

+ Above, T(n) is of the form (y = mx + c), at very large values of x, c will be insignificant
+ in comparison to mx. So, it will be a correct practice to remove (-1) from T(n).
+ T(n) = 4n
+ Still, 0 <= 4n <= 5n, where n >= 0
+ It will be a correct practice to remove 4 because 0 <= 4n <= 5n ( 0 <= T(n) <= cf(n) ) where n >= 0
+ Therefore, T(n) is still O(n)

+ Short approach :
+ worst case:
+ There are operators that run constant number of times, C1
+ There are operators that run 'n-1' number of times, C2*(n-1)
+ T(n) = C1 + C2*(n-1)
+ Removing all the lower orders of growth, constant values and constant with higher order of growth
+ T(n) = n
+ 0 <= n <= 2n, where n >= 0
+ Hence, 0 <= T(n) <= cf(n), for all n >= n`
+ Therefore, T(n) is O(n)
+ Hence, for n inputs, the maximum number of operations will be less than or equal to constant multiples of n.

+ It can also be written :
+ upper bound : O(n^2)
+ Lower bound : Ω(log n)
```

## In class portion

### Group members

List the members of your group member below:

    * Name
    * ex. Samuel Vimes
    * ...

### Timing Data

Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

| Team member    				| Timing for fibonacci | Timing for sum_to_number |
| -------------- 				| -------------------- | ------------------------ |
| Samuel Vimes   				| 0.123                | 0.456                    |
| Tushardeep Singh 				| 3.0 e-06             | 0.55                     |
| 			       | 7.9 e-06 			   | 0.8                      |
| 				 | 2.06 e-05			   | 0.98                     |
|               				| 8.5 e-06             | 1.13                     |
| 			 			| 4.74                 | 0.6                      |
| 							| 4.99 e-06			   | 1.29					  |		
					     
### Summary

| function      | fastest 		  | slowest 		| difference 								   |
| ------------- | ------- 		  | ------- 		| ---------- 								   |
| sum_to_number |0.55(tushar)     | 1.29   | 0.74       								   |	
| fibonacci     |3.0 e-06(tushar) | 4.74  | 4.74(3.0 e-06 insignificant compared to 4.74)|

### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach? Write down your 
observations.



## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?<br />
-> The fastest version of the code was optimized for performance. It contained only one while loop and there was no recursion used. Usually, in deep recursion, program tends to slow down and can crash if sufficient memory isn't available. 
In slow function sum_to_goal, more 'if' statements were used as compared to faster code.
In slow function fibonacci, in every function call, the function called itself twice, which at large values of 'i' would result in a large number of function calls, hence the function runs very slowly.

2. Was there a difference in terms of usage of space resource? Did one algorithm use more/less space (memory)?<br />
-> The faster code didn't use recursion which if not always, tends to use more space resource (memory) because each function call creates a new stack frame which stores the information of function's local variables, input parameters and return address.
In contrast, in slow function fibonacci, the function called itself twice in every function call (recursion), hence utlizing more memory.

3. What sort of conclusions can you draw based on your observations?<br />
-> Some of the group members in this lab, have very less difference in their execution time, so other than the difference in approach in solving the problem, it can also be concluded that other factors, such as processor speed, memory available, number of programs already running on the machine, and even the compiler being used can have a affect on the execution speed.
The syntax of the fastest and slowest code for sum_to_goal was more or less the same, which led me to the above conclusion.

I also observed that, recursion is not the best choice if function is being designed to call itself a lot of times, because that utilizes a lot of memory and makes the function run slow.
