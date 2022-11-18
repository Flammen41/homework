f=open('myfile1.txt','w')
f.write('Hello World!\n')
f.close()

f_file = open('myfile1.txt','r')
content = f_file.read()
f_file.close()
print(content)