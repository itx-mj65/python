#  read a file 

f=open("lec3.py")
text=f.read()
print(text)
f.close()


# ther are two types of file read and write 
# read mode is default mode
# write mode is used to write in a file
# append mode is used to append in a file
# read and write mode is used to read and write in a file
#  read a file in python

f=open("lec3.py","r")
text=f.read()
print(text)
f.close()

# write a file in python
f=open("demo.txt","w")

f.write("this is a new line")

f.close()
# append a file in python
f=open("demo.txt","a")

f.write("this is another line")
f.close()

# difference btw append and write mode
# if we use write mode and file already exist then it will delete the file and write the new

# other file modes 
# r+ : read and write mode
# w+ : read and write mode
# a+ : read and write mode
# readline() function is used to read a single line from a file

line=open("demo2.text")
textline=line.readline()
print(textline, type(textline))
line.close()
# read all lines from a file

line=open("demo2.text")
alltext=line.readlines()
print(alltext, type(alltext))
line.close()

#  with statement is used to automatically close the file after use

with open("demo.txt", "r") as withstatement:
    print(withstatement.read())
