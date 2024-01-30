'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3,5,6 and 9. The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
'''

# Problem 1 Function
def Problem1():
    # As the input is always 1000, we don't need to cater for a generic usecase (x or n)
    # var to store the total sum we need to print at the end
    sum = 0
    # I started from 1 as 0 is not a natural number when counting
    for i in range(1,1000):
        # check whether the number is a multiple of both 3 and 5
        if i % 15 == 0:
            sum += i
        # check whether the number is a multiple of 3
        elif i % 3 == 0:
            sum += i
        # check whether the number is a multiple of 5    
        elif i % 5 == 0:
            sum += i
    
    return sum


# Main Function
if __name__ == "__main__":
    sum = Problem1()
    print("The sum of all multiples of 3 and 5 below 1000: ", sum)