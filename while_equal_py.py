list=[10,20,30,40,50]
n=len(list)-1
while n>=0:
    if list[n]==30:
        print("the no which are looking for present")
        n=n-1
        continue
    print(list[n])
    n=n-1