

def factorial(x):
    fact=1
    for i in range(1,x+1):
        fact=fact*i
    return fact

def permutation(n,r):
    if r>n:
        print("No such combination")
    else:
        result=factorial(n)/factorial(n-r)
    return result

num = int(input("Enter the value of n : "))
r = int(input("Enter the value of r: "))
print(permutation(num,r))
