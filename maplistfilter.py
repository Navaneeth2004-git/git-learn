l1=[1,2,3,4,5]
def multiply(x):
    return x*2
    
result=map(multiply,l1)
print(list(result))







l1=[1,2,3,4,5]
def multiply(x):
    return x%2
    
result=filter(multiply,l1)
print(list(result))