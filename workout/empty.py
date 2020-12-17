str1=input("Enter string:")
sub=input("enter substring:")
pos=-1
bal=False
n=len(str1)
while True:
    pos=str1.find(sub,pos+1,n)
    if pos==-1:
        break
    print(sub,"presentat",pos)
    bal=True
if bal==False:
    print("data not found")

