string=input("enter string to count letters:")
length=len(string)
s={""}
for ch in string:
    time=0
    for ind in range(0,length):
        if ch==string[ind]:
            time=time+1
    char_times=ch+" "+ "is present "+str(time)
    s.add(char_times)
print(s)
#for i in s:
 #   print(i)

