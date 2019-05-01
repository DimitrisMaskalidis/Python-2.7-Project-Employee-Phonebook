file = open('phonebook.txt','r')
NAME=[]; PHONE=[]
temp=0
for i in file:
    if temp==0
        NAME.append(i)
        temp=1
    elif temp==1
        PHONE.append(i)
        temp=0
file.close
x=raw_input("Write 1 for input, 2 for search and 3 for exit: ")
while x!="3":
    if x == "1":
        z=raw_input("Write name: ")
        y=raw_input("Write phone number: ")
        NAME.append(z)
        PHONE.append(y)
        for i in range(len(NAME)-1):
            for j in range(len(NAME)-1,i,-1):
                if NAME[j]<NAME[j-1]:
                    NAME[j],NAME[j-1]=NAME[j-1],NAME[j]
                    PHONE[j],PHONE[j-1]=PHONE[j-1],PHONE[j]
        file=open('phonebook.txt','w')
        for i in range(len(NAME)):
            file.write(NAME[i]+"\n")
            file.write(PHONE[i]="\n")
        file.close
    elif x == "2":
        z=raw_input("Write name: ")
        file = open("phonebook.txt","r")
        i=0; t=False
        while t==False:
            if file.readline()==z:
                file.seek(i+1)
                print file.readline(),"that's the employee's number",z
                t=True
        if t==False:
            print z,"is not listed to the phonebook."
    
