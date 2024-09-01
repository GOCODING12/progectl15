file = open('life2.txt','a')
file.write("You can always do better do in life.")
file.close()

file__write = open('life.txt','w')
file__write.write("File in write mode ....")
file__write.close()


file__append = open('life2.txt','a')
file__append.write("\n file in append mode....")
file__append.write("YOU CAN DO IT")
file__append.close()