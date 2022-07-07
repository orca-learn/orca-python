# https://www.w3schools.com/python/python_datatypes.asp


"""
Built-in Data Types

Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType

"""

x = 5
print(type(x))

x = "Hello World"
print(type(x))

x = 20
print(type(x))

x = 20.5
print(type(x))

x = 1j
print(type(x))

x = ["apple", "banana", "cherry"]
print(type(x))

x = ("apple", "banana", "cherry")

x = range(6)

x = {"name" : "John", "age" : 36}

x = {"apple", "banana", "cherry"}

x = frozenset({"apple", "banana", "cherry"})

x = True

x = b"Hello"

x = bytearray(5)

x = memoryview(bytes(5))

x = None