fh=open("hello.txt","w+")

ch=input("read or write(r/w)")

str1=input("string:")
fh.writelines(str1)
print(fh.tell())
fh.seek(0)
print(fh.readline())

fh.close()