print("Python Eval Even")
Tasks={"Name":[ 1 ,"Status"]}

print("Enter 1 to Insert new Task, 2 to Modify Status, 3 to Delete a Task, 4 to List all tasks, 5 to search for tasks, Listing tasks according to last letter")

n=int(input("Enter your choice"))

if(n==1):
    name=input("Enter task name:")
    id=int(input("Enter task ID:"))
    status=input("Pending/Completed?:")
    Tasks[name]=[id, status]
    for x,y in Tasks.items():
        print(x,":",y)

elif(n==2):
    name=input("Enter the name of task you want to modify status of:")
    status=input("enter the modified status:(Pending/Completed):")
    id=int(input("Enter its ID"))
    Tasks[name]=[id, status]
    for x,y in Tasks.items():
        print(x,":",y)
    
elif(n==3):
    name=input("Enter the name of task you want to delit:")
    del Tasks[name]
    for x,y in Tasks.items():
        print(x,":",y)
    
elif(n==4):
    for x,y in Tasks.items():
        print(x,":",y)
        
elif(n==5):
    name=input("Enter the task name to be searched:")
    for x,y in Tasks.items():
        if(x==name):
            print(x,":",y)
        else:
            print("No such Name exists:")
            
else:
    i=input("Enter the suffix:")
    for x,y in Tasks.items():
        for j in x:
            if(x[-1]==i):
                print(x,":",y)
                
                
            
            
    
    
    
