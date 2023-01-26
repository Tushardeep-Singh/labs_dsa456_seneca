```diff
-Changes to this file will be made on or before january 28th 2023 
```
# Lab 2
```diff
+ Author: Tushardeep Singh
+ Student Number: 160427217
```


### function 1:

Analyze the following function with respect to number
```diff
+ Let 'number' be the input/parameter to function1(), wherein a series of calculations 
+ will be done using 'number' and a return value will be generated.
+ For analysis, let n = number. Then, loop will iterate 'n' number of times (0 to n-1 both inclusive)
+ Let T(n) represent the total number of operations required to generate a return value,
+ where 'n' is the range of 'for' loop used below.
```

```python
def function1(number):
	total=0; # 1

	for i in range(0,number): # n + 1
		x = (i+1) # 2n
		total+=(x*x) # 2n

	return total # 1
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
	return  ((number)*(number+1)*(2*number + 1))/6 # (1) + (1) + (1) + (1+1) + (1) + (1)

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
+ i.e 0 <= T(n) <= cn is true for all n >= n`
+ Therefore, T(n) is O(n)
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
	for i in range (0,len(list)-1): # (n-1) + 1 + 1
		for j in range(0,len(list)-1-i): # z + (n-1) + 1 + 1 + (n-1)
			if(list[j]>list[j+1]): # 2z
				tmp=list[j] # z
				list[j]=list[j+1] # 2z
				list[j+1]=tmp # 2z

```
```diff
+ T(n):
+ Total number of operations required to order the list in ascending order:
```
![complete calculation](https://user-images.githubusercontent.com/113130891/213402453-53bd25e1-9db1-456f-aa31-3714fb955a3a.jpeg)

### function 4:

<!-- this function calculates factoral. -->

Analyze the following function with respect to number

```python
def function4(number):
	total=1
	for i in range(1 to number):
		total=total*(i+1)
	return total
```

## In class portion

### Group members

List the members of your group member below:

    * Name
    * ex. Samuel Vimes
    * ...

### Timing Data

Note, if a groupmate did not complete lab1, simply put 0.0 in for the times, it is ok if there is something missing.

| Team member    | Timing for fibonacci | Timing for sum_to_number |
| -------------- | -------------------- | ------------------------ |
| Samuel Vimes   | 0.123                | 0.456                    |
| group member 2 | 0.0                  | 0.0                      |
| group member 3 | 0.0                  | 0.0                      |
| group member 4 | 0.0                  | 0.0                      |
| group member 5 | 0.0                  | 0.0                      |
| group member 6 | 0.0                  | 0.0                      |

### Summary

| function      | fastest | slowest | difference |
| ------------- | ------- | ------- | ---------- |
| sum_to_number |         |         |            |
| fibonacci     |         |         |            |

### Discussion:

Look at the code from lab 1 and discuss the differences between fastest/slowest versions. Was it a difference in syntax? A difference in approach? Write down your observations.

## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?
2. Was there a difference in terms of usage of space resource? Did one algorithm use more/less space (memory)?
3. What sort of conclusions can you draw based on your observations?
