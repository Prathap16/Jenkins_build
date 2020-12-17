string1=input("enter string to sort:")
alpa_result=""
num_result=""
for ch in string1:
    if ch.isalpha():
        alpa_result=alpa_result+ch
    else:
        num_result=num_result+ch
result_list=sorted(alpa_result)+sorted(num_result)
output=""
for ch in result_list:
    output=output+ch
print(output)


