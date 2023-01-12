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

#Write a Python function called num_within() to check whether a number falls in a given range.
def num_within(a,b,c):
    return a in range(b,c+1)

print(num_within(3,2,4))
print(num_within(3,1,3))
print(num_within(10,2,5))

