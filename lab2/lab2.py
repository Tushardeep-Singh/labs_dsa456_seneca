# copy over your code from lab 1 to this file


# function name: fibonacci
# input: a non-negative integer n
# returns nth fibonacci number
def fibonacci(n):
    seq_01 = [0,1] #seq_01 list contains fibonacci_0 and fibonacci_1

    if(n == 0):
        return seq_01[0]

    if(n == 1):
        return seq_01[1]

    # the nth fibonacci number is the sum of the 2 previous fibonacci numbers.
    # below, before while loop, pre_digit and pre_pre_digit i.e. previous 2 digits have been assigned for fibonacci_3
    pre_digit = seq_01[1] #1
    pre_pre_digit = seq_01[0] #0
    start = 3
    result = pre_digit + pre_pre_digit; #fibonacci_2 = 1

    if(n == 2):
        return result

    pre_pre_digit = pre_digit #1
    pre_digit = result #1
    
    while(start <= n): #loop begins at 3
        result = pre_digit + pre_pre_digit;
        pre_pre_digit = pre_digit
        pre_digit = result
        start += 1
    return result

    

#function name: sum_to_goal
#inputs: number_list which is list of numbers, goal_val which is a number
#This function finds the two numbers in the list that sum up to the goal value. Function returns the product of the two numbers(the product is the result of multiplying the two numbers together) . If there are no two numbers that when summed results in the goal state, function returns 0
def sum_to_goal(number_list,goal_val):
    list_len = len(number_list)

    for x in range(0,list_len):
        for y in range(0,list_len):
            sum_2 = (number_list[x] + number_list[y])
            if(sum_2 == goal_val):
                result = number_list[x] * number_list[y]
                return result
            else:
                continue
    
    return 0


    