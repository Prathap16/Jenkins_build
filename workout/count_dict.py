char_dic={}
string1="raman"
for ch in string1:
    if ch not in char_dic:
        char_dic[ch]=0
    char_dic[ch]+=1
print(char_dic)
char_dic=dict(sorted(char_dic.items(), key=lambda item: item[1], reverse=True))
for key,value in char_dic.items():
    print(key,"-----",value)