details_dict={}
num_std=int(input("Enter number of students:"))
for sno in range(1,num_std+1):
    print(sno,"students details:-")
    name=str(input("\tEnter Student Name:")).lower()
    marks=int(input("\tEnter student marks:"))
    details_dict[name]=marks
while True:
    st_d=input("Enter student name to get details:").lower()
    if st_d in details_dict.keys():
        print(st_d.title(),"Marks:",details_dict[st_d])
        if details_dict[st_d]<35:
            print("results: Fail")
        else:
            print("results: Pass")
        other_details=input("Do you want to know one more student details?(yes|no):")
        if other_details.lower()=="no":
            break
        elif other_details.lower()=="yes":
            continue
        else:
            print("you did not enter (yes or no)!! please enter your response properly")   
    else:
        print(st_d,"student details are not exists!")
print("Thanks for using Student App!!")
