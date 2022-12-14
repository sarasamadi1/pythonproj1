from math import sqrt

#defining our function
def prime_num(number):
    #checking if the number is less than 2 or divisible by 2
    if (number < 2 or number % 2 == 0):
        return (number == 2)
    divisor = 3
    #checking if each squar root of number in our main body is greater than 3 or not
    while (divisor <= sqrt ( number )):
        #if it was, we should check if it is divisible by 3 or not
        if (number % divisor == 0) :
            return False  #reterning false if it is divisible by 3
        else :
            divisor += 2  #if it's not, then we increase 3 by 2 each time
    return True
res = set()  #saving each wanted number

for k in range(17):
    for l in range(17):
        if prime_num(2**k + 3**l):      #passing values to our function
            res.add(2**k + 3**l)        #adding each new number
print(*sorted(res),sep=", ")
