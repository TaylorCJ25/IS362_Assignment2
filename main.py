# **Assignment 2**
import markdown
output = markdown.markdown('''
# **Assignment 2**
## *Zip Function and Description*
### The zip function allows for a zip object to be returned. This can be in the form of an iterator of tuples where items from each iteratoris paired together and so on.
### below I show an example of a zip file by combining iterator: Name and Iterator: Line Position.

''')

Name = ("Nick", "Heather", "Katherine")
Line_position = ("1", "2", "3")

Line_Order = zip(Name, Line_position)
print (output)
print (tuple(Line_Order))
