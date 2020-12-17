import os,sys
words=[]
char_count=0
file_name=input("Enter file name :")
if os.path.isfile(file_name):
    with open(file_name,"r") as f:
        data=f.readlines()
        data=[x.strip("\n") for x in data if x.isspace()==False ]
        print(data)
        for line in data:
            words.extend(line.split())
            line=line.replace(" ", "")
            print(line)
            char_count=char_count+len(line)
        number_of_line=len(data)
        number_of_words=len(words)
        print(words)
        print("number of  lines in "+file_name+" file:",number_of_line)
        print("number of  words in "+file_name+" file:",number_of_words)
        print("number of charectors in "+file_name+" file:",char_count)
else:
    print(file_name,"does not exists. please check!")
