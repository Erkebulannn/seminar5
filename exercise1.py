try:
    Erke = open("mailbox.txt")
except:
    print('File cannot be opened')
    exit()

lines=Erke.readlines()
file=open('output.txt', 'w')
for line in lines:
    if 'Details:' in line:
        ind=line.find('?view=rev&rev=')
        en_ind=line.find(';')
        word=line[ind+14:en_ind]
        print(word) 
        file.write(word)
        file.write('\n')
Erke.close()
file.close()
