
# with open("data.txt","r") as file :
#         print(file.readline(), end="")
#         print(file.readline(), end="")
#         print(file.readline(), end="")

# file= open("data.txt", "w")
# file.write("\nLLO PYTHON")
# file.write("shristi\n")
# file.write("PYTHON\n")
# file=file.close()

# file=open("data.txt","r")
# print(file.read())

# with open("data.txt","r") as file:
#         lines = file.readlines()
#         print(lines)

# with open("data.txt","r")as file:
#     lines = file.readlines()
# for line in lines:
#     print(line.strip())

# lines= ["hii\n" , "banana\n" , "water\n " , "mango\n" , "cat\n" , "sound\n"]
# # with open("data.txt" , "w") as file :
# #     file.writelines(lines)
# print(lines)

# with open("data.txt","r")as file:
#     lines=file.readlines()  
#     print(lines[:2])

# with open("data.txt","r")as file:
#     lines=file.readlines()
#     print(len(lines))


# with open("data.txt","r")as file:
#     for line in file:
#         if "mango" in line:
#             print(line.strip())

# file=open("shrish.txt","w")
# file.write("hello")
# file=file.close()

# def student_intro(a,b,c,d,e):
#     print("student introduction")
#     print("name:", a)
#     print("class:", b)
#     print("school:", c)
#     print("city:", d)
#     print("hobby: ",e)

# student_intro ("shristi","it" ,"xyz","delhi","abc")

# def num(a="user"):
#     if a%2==0:
#         print("number is even", a)
#     else:
#         print("number is odd", a)  
# num(13)

# def tab_le(a="user"):
#    for i in range(1,11):
#     print(a,"x",i,"=",a*i)
# tab_le(14)


def cal(a,b):
    operator = input("enter any operator +,-,*,/")
    if operator =="+":
        print(a+b)
    elif operator =="-":
        print(a-b)
    elif operator =="/":
        print(a/b)
    elif operator =="*":
        print(a*b)
cal(10,12)
