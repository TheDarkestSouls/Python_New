s=input("enter H or T as many times as wanted: ")
t=0
while "T"*(t+1) in s:
    t+=1
if t!=0:
    print(t)
else:
    print(0)
