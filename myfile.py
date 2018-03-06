f1=open("file1.py",'r')
words = f1.read()
f1.close()

m=words.split()
n=len(words.split())

print('The splited words are:',m)
print('The word count is:',n)

a=words.count(0)
print(a)




