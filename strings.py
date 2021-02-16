myStr = "Hello"

#print(dir(myStr))

# print(myStr.upper())
# print(myStr.swapcase())
# print(myStr.replace("Hello", "Adios").upper())
# print(myStr.count("l"))
# print(myStr.startswith("H"))
# print(myStr.endswith("o"))

print(myStr.split("e"))
print(myStr.find("l"))
print(len(myStr))
print(myStr.index("H"))

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[3])
print(myStr[-1])
#la "F" es para que interprete la variable en el print
print(f"El texto es {myStr}")