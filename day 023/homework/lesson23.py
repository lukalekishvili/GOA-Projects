# 1 
def func(x,x1):
    if type(x) or type(x1)==bool:
        return 'error'
    if type(x)==float:
        return int(x1) + x
    if type(x1)==float:
        return int(x) + x1
    else:
        return int(x) + int(x1)

print(func(1,1.2))
