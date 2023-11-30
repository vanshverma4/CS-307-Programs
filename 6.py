#program 6


dict1=dict()

def addiemsindict(a,b,c):
    dict1[a]={"Faculty":b,"Student":c}

while 1==1:
    deptname=input("Enter the name of department : ")
    fname=input("Enter the name of the faculty : ")
    sname=input("Enter the name of the student : ")
    addiemsindict(deptname,fname,sname)
    choice=int(input("are you done(1 for yes , 0 for no) : "))
    if(choice==1):
        break
    else:
        pass
print(dict1)

student_list=[]
faculty_list=[]

for i in dict1.keys():
  student_list.append(dict1[i]["Student"])
  faculty_list.append(dict1[i]["Faculty"])

print("Student List : ",student_list)
print("Faculty List : ",faculty_list)

if "SOA" not in dict1.keys():
  print("not found")
  dict1["SOA"]={"Faculty":"K","Student":"L"}
  print("added")
else:
  print("found")