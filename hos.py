import pickle

hos={}
isrun=True

while isrun==True:
    choice=input("do you want to read  write new data(r/w):")
    if choice=='r':
        with open("hos.dat","rb") as fh:
            fh.seek(0)

            try:
                st=' '
                while st:   
                    print(pickle.load(fh))
            except EOFError:
                fh.seek(2)
    elif choice=="w":
        with open("hos.dat","ab") as fh:
            fh.seek(2)
            iter=int(input("how many entries:"))

            for i in range(iter):
                n=input("name:")
                spec=input('speciality:')
                sal=int(input("salary"))
                hos["Name"]=n
                hos["Speciality"]=spec
                hos["salary"]=sal

                pickle.dump(hos,fh)
                fh.flush()
                print("Data Entered")
    elif choice=='s':
        field=input('enter the field name:')
        sk=(input("enter what do you want to search:"))
        l=[]
        l.insert(0,sk)
        print(sk)
        with open("hos.dat","rb") as fh:

            fh.seek(0)
            try:
                while True:
                    hos=pickle.load(fh)
                    if hos[field] in l:
                        print(hos)

            except EOFError:
                pass
    else:
        print('invalid data')
        isrun=False
     
