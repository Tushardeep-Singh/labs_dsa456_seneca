```diff
-Changes to this file will be made on or before january 28th 2023
```
# Lab 2 
```diff
+ Author: Tushardeep Singh
+ Student Number: 160427217
```

## Due: Jan 28

## Objectives:

-   Learn how to perform analysis

## Setup


All files needed for this lab were created by doing the first task in [lab 0](lab-00.md).  If you didn't do lab 0, do the first task to create your lab repository.

Unless otherwise stated, all writing goes into the file lab2.md

## Part A Analysis


-   Perform an analysis of the following functions:

### function 1:

Analyze the following function with respect to number
```diff
+ Let 'number' be the input/parameter to function1(), wherein a series of calculations 
+ will be done using 'number' and a return value will be generated.
+ For analysis, let n = number. Then, loop will iterate 'n' number of times.
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

Analyze the following with respect to the length of the list.  Note that the function call len() which returns the length of the list is constant (O(1)) with respect to the length of the list.
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

Analyze the following function with respect to number

```python
def function4(number):
	total=1
	for i in range(1, number):
		total*=(i+1)
	return total
```

## Part B Pre-Lab Preparation:

While not 100% required, doing this will make it easier to complete the lab during the lab class

-   Push your lab1.py from lab 1 into your lab 2 repository.

## Part C In-Lab Discussion:

-   During your lab period, form groups of 5 to 6 students.
    -   Your professors may have further instructions on how to form groups.
-   If you have not completed the pre-lab, do so now. copy your lab1.py from lab1 into your lab2 repo and push it into github.  Do not change name of file, keep it as lab1.py
-   Doing so will trigger a series of tests which will be timed.
-   In each group, look at your runs your lab1 functions (using lab2's set of testers)
    -   In the action tab, expand your successful run of the tester for the lab. you will find the timing results of your functions there.
    -   in lab2.md discussion, fill in the names of your group members.
    -   Fill in the Timing table in lab2.md with the times for your group, add or remove rows as necessary based on the number of members in your group

    -   Fill in the second table with the following information:

        -   slowest time for each of the listed function
        -   fastest time for each of the listed function
        -   difference in timing between slowest and fastest times

    -   Compare the slowest and the fastest version of each function, what were the differences? Was it a difference in syntax? A difference in approach?... for example, did one solution use recursion while the other did not?

## Reflection

1. Considering the solutions you saw when looking at the lab 1 code, what differences did you see between fastest and slowest versions of code?
2. Was there a difference in terms of usage of space resource?  Did one algorithm use more/less space (memory)?  
3. What sort of conclusions can you draw based on your observations?

## Submitting your lab

In order to get a mark for this lab, you must submit:

-   a complete analysis of every function in part A.

Please make sure you follow the steps listed below fully

- Place all your work for this lab into the file lab2.md unless otherwise indicated


## Lab Rubric:

| Criteria       | Poor - 0 mark     | Fair - 0.5 marks                                                                                                                     | Good - 1 marks                                                              |
| -------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------- |
| Lab Completion | No analysis present/completed | An analysis was present but was missing key steps or a properly completed analysis but no group work participation and/or reflection | Successfully complete both the group portion of the lab and the reflection. |
