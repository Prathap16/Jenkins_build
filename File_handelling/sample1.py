import os,sys
os.system("lscpu>lscpu.out")
print("++++++++++printing directories and files in current path in list format++++++++")
print("\n")
print(os.listdir("."))
#file opening with read bu with block
with open("lscpu.out","r") as f:
    #creating list from given file as one line is equal to one item by using readlines()
    lines_list=f.readlines()
    #itirating lines_list and removing \n at tailing area of each item and split that item into list by seperator ":"
    lines_list=[line.strip("\n").split(":") for line in lines_list]
    len_lines_list=len(lines_list)
    #removing the tailing area of elements in lines_list
    for i in range(0,len_lines_list):
        lines_list[i][1]=lines_list[i][1].strip()
    #converting lines_list into dictonary by using dict()
    dict_info=dict(lines_list)
print("\n")
print("+++++++Printing Dictonary of values taken form lscpu command++++++++")
print("\n")
print(dict_info)
print(len(dict_info))




with open("lscpu.out","r") as f:
    #creating list from given file as one line is equal to one item by using readlines()
    lines_list=f.readlines()
    lines_list=
    #itirating lines_list and removing \n at tailing area of each item and split that item into list by seperator ":"
    lines_list=[tuple(line.strip("\n").split(":")) for line in lines_list]
    len_lines_list=len(lines_list)
    #removing the tailing area of elements in lines_list
    for i in range(0,len_lines_list):
        lines_list[i][1]=lines_list[i][1].strip()
    #converting lines_list into dictonary by using dict()
    dict_info=dict(lines_list)
print("\n")
print("+++++++Printing Dictonary of values taken form lscpu command++++++++")
print("\n")
print(dict_info)
print(len(dict_info))










