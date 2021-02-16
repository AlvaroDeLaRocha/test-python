demoList = [1, "hello", 1.34, True, [1, 2, 3]]

numbersList = list((1, 2, 3, 4))
#print(numbersList)
colors = list(("blue", "yellow", "purple"))
r = list(range(1, 10))
print(r)
print(len(r))
#Imprimir si "2" esta en la lista
print(2 in r)

r[1] = "yellow"
print(r)

r.append((77, 88))
print(r)

colors.extend(("green", "red"))
print(colors)

colors.insert(1, "black")
print(colors)

colors.insert(len(colors), "violet")
#Quita el ultimo elemento de la lista o con el indice marcado
colors.pop(1)
print(colors)

colors.remove("red")
print(colors)

# colors.clear()
# print(colors)

colors.sort(reverse=True)
print(colors)

print(colors.index("blue"))
print(colors.count("blue"))