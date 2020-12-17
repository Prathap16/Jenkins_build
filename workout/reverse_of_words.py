stat=input("Enter string:").split()
#print(type(stat))
stat_list=[string.strip(".|!|,") for string in stat]
#print(stat_list)
result_list=[]
for word in stat_list:
    rev_word=word[::-1]
    result_list.append(rev_word)
#print(result_list)
#final_str=""
#for value in result_list:
#    final_str=final_str+" "+value
#print(final_str.strip())
final_str=" ".join(result_list)
print(final_str)
