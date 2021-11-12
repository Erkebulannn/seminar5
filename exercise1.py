fin=open('mailbox.txt')

lines=fin.readlines()
file=open('output.txt', 'w')

for line in lines:
   if 'Details:'in line:
     print(line[-6:-1])
     file.write(line[-6:-1])
     file.write('\n')
fin.close()
file.close()


