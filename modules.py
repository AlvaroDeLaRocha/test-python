import datetime
from datetime import timedelta, date
# importe el modulo desde otra clase
import mymath
# Modulo para cambiar de color la letra
from colorama import Fore, Style, init
init(convert = True)
print (Fore.BLUE + "colorama")

print(datetime.date.today())
# print(datetime.timedelta(minutes=200))
print(timedelta(minutes=200))

mymath.add(1,2)