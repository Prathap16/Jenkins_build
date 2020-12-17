str1=input("enter 1st string:")
len1=len(str1)
str2=input("enter 2nd string:")
len2=len(str2)
result=""
for index1, char1 in enumerate(str1):
    for index2, char2 in enumerate(str2):
        if index1==index2:
            result=result+char1+char2
#print(char)
if len1 > len2:
    result=result+str1[len2:len1]
if len1 < len2:
    result=result+str2[len1:len2]
print(result)
