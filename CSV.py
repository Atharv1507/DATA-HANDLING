import csv

fh = open('emp0.csv', 'w+', newline='')
wr = csv.writer(fh, delimiter='|')
r = csv.reader(fh)  # Open for reading



print("Existing data in the file:")
fh.seek(0)
for i in r:
    print(i)

ent = int(input('enter no. of entries:'))

for i in range(ent):
    n = input('enter name:')
    s = int(input('enter sal:'))
    d = input('enter department:')
    l = [n, s, d]
    wr.writerow(['NAME', 'SAL', 'DEPARTMENT'])
    wr.writerow(l)
    print(l)

fh.close()
