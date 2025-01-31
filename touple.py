a=(22,"ali",27.66)

print(type(a))

# this is a tuple and can't be changed once defined. it is immutable.
# tuples are defined by enclosing elements in parentheses, ( ) and are ordered. they can contain any
# data type, including strings, integers, floats, and other tuples. they are often used to
 # group related data together.
 # tuples are faster than lists because they are immutable. they are also more memory efficient.
 # tuples are often used when you need to store a collection of data that will not change. they
 # are also used when you need to return multiple values from a function. 

b=("ali","adeel",22, 20.07,"bahawal","ali")
print(len(b))
print(b.index("adeel"))
print(b.count("ali"))
