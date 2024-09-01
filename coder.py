#open file and read its contents
file = open('life.txt','r')
print(file.read())
file.close()

file = open('life.txt','r')
print('\n read in parts\n')
print(file.read(8))
file.close()