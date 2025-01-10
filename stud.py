import pickle as p
fh=open('STUD.dat','ab+')
y=int(input('enter no. of entries:'))
st={}
try:
    for i in range(y):
        n=input('enter name')
        r=int(input('enter roll'))
        f=int(input('enter fees'))
        d=input('enter dob')
        st['Name']=n
        st['roll']=r
        st['fees']=f
        st['DOB']=d
        p.dump(st,fh)
    
    fh.seek(0)
    while True:
        x=p.load(fh)
        print(x)
except EOFError:
    fh.close()