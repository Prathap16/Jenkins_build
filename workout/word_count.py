stat=input("enter your statement:")
stat_list=[word.strip(",|.|!").upper() for word in stat.split()]
print(stat_list)
length=len(stat_list)
s={"+++++++++++++++++++++++++++"}
for obj in stat_list:
    time=0
    for ind in range(0,length):
        if obj==stat_list[ind]:
            time=time+1
    a=obj+" "+"is present "+str(time)+"times"
    s.add(a)
for i in s:
    print(i)



    
