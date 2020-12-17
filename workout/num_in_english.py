num=input("enter number to convert in english:")
eng_num=""
eng_list=["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
for i in num:
    eng_num=eng_num+" "+eng_list[int(i)]

print(num,"in english is",eng_num)

 