# Write the code for your lab 1 here.  Read the specs carefully.  
# Function name must be exactly as provided.  
# Names of variables and parameters can be whatever you wish it to be
#
# To test, run the following command :
#     python test_lab1.py
#
# Author: Tushardeep Singh
# Student Number: 160427217
#


# function name: wins_rock_scissors_paper
# inputs: string player, string opponent
# returns a boolean value as per rock paper scissors hand game rules: https://wrpsa.com/the-official-rules-of-rock-paper-scissors/ (read : What are the rules of RPS?)
# .lower() : To compare alternating caps
def wins_rock_scissors_paper(player,opponent):
    if(player.lower() == "rock" and opponent.lower() == "scissors"):
        return True
    elif(player.lower() == "paper" and opponent.lower() == "rock"):
        return True
    elif(player.lower() == "scissors" and opponent.lower() == "paper"):
        return True
    elif(player.lower() == opponent.lower()):
        return False
    else:
        return False
	

# function name: factorial
# inputs: integer int_n
# returns int_n! if int_n > 0. If int_n == 0, returns1
def factorial(int_n):
    int_x = 1
    const_y = int_n
    fact = const_y

    if(int_n == 0):
        return 1

    while(int_x < int_n):
        fact = fact * (const_y - int_x)
        int_x += 1
    return fact


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
	

# class : UpCounter
class UpCounter:
    counter = 0 #counter=0 for every object created

    # If no step_size mentioned, then self.step_size = 1
    def __init__(self):
        self.step_size = 1

    def __init__(self,step_size):
        self.step_size = step_size
    
    def count(self):
        return self.counter
    
    def update(self):
        self.counter += self.step_size
        


# class : DownCounter
class DownCounter(UpCounter):
    def update(self):
        self.counter -= self.step_size
    



