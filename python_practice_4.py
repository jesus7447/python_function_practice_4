#Write a Python function called max_num()to find the maximum of three numbers
def max_num(a,b,c):
    return max([a,b,c])
print(max_num(20,8,19))

#Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(num):
    
    if num == 1:
        return 1
    return (num * mult_list(num - 1))
n=10
print(mult_list(n))

#Write a Python function called rev_string() to reverse a string.
def rev_string(x):
    return x[::-1]

string = rev_string('I am backwards')
print(string)