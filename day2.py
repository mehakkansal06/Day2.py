a=int(input("enter your age"))
if a>18:
    print("eligible to vote")
elif(a==18):
    print("wait for some time")
else:
    print("try next time")        
    
    
    
a=int(input("enter your marks"))
if a>100:
    print("invalid")
elif a>=90:
    print("A+ grade")
elif a>=75:
    print("A grade")
elif a>=60:
    print("B grade")
elif a>= 40:
    print("C grade")
elif a>= 0:
    print("fail")                 
else :
    print("not possible")       