def calculator(n1,n2,op):
    if op=='+':
        return n1+n2
    elif op=='-':
        return n1-n2
    elif op=='*':
        return n1*n2
    elif op=='/':
        return n1/n2
    else:
        return 'Invalid operation'

n1=int(input("Enter first number:"))
op=input("Enter the operation:")
n2=int(input("Enter second number:"))
print(calculator(n1,n2,op))