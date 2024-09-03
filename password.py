import random
def passwordgenerate(n):
    charecter='abcdefABCD1234#'
    password=''
    for i in range(n):
        password+=random.choice(charecter)
    return password    
a=int(input('enter length'))
print(passwordgenerate(a))