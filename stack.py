def push():
    inp=input("what would you like to add")
    st.append(inp)
    print ('successfully added')    
def peek ():
    if st==[] :
        print("Cannot perform action stack is empty")
        IsTrue=False
    else:
        x=len(st)
        print(st[x-1])
def pop():
    if st==[] :
        print("Cannot perform action stack is empty")
        IsTrue=False
    else:
        x=len(st)
        st.pop(x-1)

def display():
    if st==[]:
        print("empty list")
    else:
        x=len(st)
        for i in range(x-1,-1,-1):
            if i ==x-1:
                print(st[i],'\t <--top element')
            else:
                print(st[i])
        
st=[]
isTrue=True
print('welcome to stack')
print('There are 4 available functions\n 1.push\n 2.peek\n 3.pop\n 4.display stack\n 5.exit')
while isTrue==True:
    opt=int(input('enter function no:'))
        
    if opt==1:
            push()
    if opt==2:
            peek()
    if opt==3:
            pop()
    if opt==4:
            display()
    if opt==5:
        isTrue=False    
        
