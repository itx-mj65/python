# loops 

i=0
# while i<20:
#     print(i)
#     i+=1

# b=[9887,65,"harry", "black", "white"]
# while i<len(b):
#     print(b[i])
#     i+=1

#  for i in range
# for j in range(10):
#     print(j)  

# c=[68,976,975,"ali"]
# for j in c:
#     print(j)

# d=(10, 27,972,869)

# for j in d:
#     print(j)
# else:
#     print("this loop is over")

#  break and continue
for i in range(10):
    # if i==5:
    #     break
    # print(i)

    if i==3:
        continue
    print(i)

 # pass in loop
for i in range(10):
 
        pass

print("after pass")
n=int(input("enter the number of  tables"))

for table in range(11):
     print(f"{n} X {table} = {n*table}")

# starts with in for loop
names=["Adeel","Bahawal","Ali"]

for name in names:
     if(name.startswith("A")):
          print(name)