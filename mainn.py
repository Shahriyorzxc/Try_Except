#=========================================ZeroDivisionError===============================================================================================

try:
    res = 10 / 0
except ZeroDivisionError as l:  #ZeroDivisionError: Вызывается, когда происходит деление на ноль.
    print(f"Result: {l}")

#=========================================TypeError===============================================================================================

try:
    res1 = "dota" + 10
except TypeError as lp: # TypeError: Вызывается, когда операция применяется к объекту несоответствующего типа.
    print(f"Error: {lp}")

#===========================================ValueError=============================================================================================

try:
    num = int("Son: ")
except ValueError as lk: # ValueError: Вызывается, когда функция получает аргумент правильного типа, но с недопустимым значением.
    print(f"Error: {lk}")

#===========================================IndexError =============================================================================================

try:
    lst = [1,2,3,4,5]
    print(lst[6])
except IndexError as i: # IndexError: Вызывается, когда индекс последовательности находится за пределами допустимого диапазона.
    print(f"Error: {i}")

#============================================KeyError============================================================================================

try:
    dict1 = {"a": 1, "b": 2, "c": 3}
    print(dict1["d"])
except KeyError as d:  #KeyError: Вызывается, когда ключ не найден в словаре.
    print(f"Error: Key {d} was not found")

#=========================================FileNotFoundError===============================================================================================

try:
    with open("file.txt" "r") as try_except:
        l = try_except.read()
except FileNotFoundError as f: # FileNotFoundError: Вызывается, когда файл или директория не найдены.
    print(f"Error: {f}")

#==========================================ImportError==============================================================================================

try:
    import dota_2
except ImportError as a: # ImportError: Вызывается, когда не удалось импортировать модуль или имя модуля не найдено.
    print(f"Error: {a} was not found")

#==========================================AttributeError==============================================================================================
class Car:
        def __init__(self, bmv):
            self.bmv = bmv

        def Mers(self):
           print(self.Porche)
try:
    obj = Car(1)
    print(obj)
    print(obj.not_excited)
except AttributeError as c: # AttributeError: Вызывается, когда атрибут объекта не существует или не может быть использован.
    print(f"Error: {c}")

#=======================================SyntaxError=================================================================================================
try:
    x = 17 +
    print(x)
except SyntaxError as x1: # SyntaxError: Вызывается, когда обнаружена синтаксическая ошибка в коде.
    print(f"Error: invalid syntax {x1}")


#======================================== IndentationError================================================================================================
try:
    if True:
        print("Hello World")
except IndentationError as k: # IndentationError: Вызывается, когда обнаружена ошибка в отступах.
    print(f"Error: {k}")

#===========================================OverflowError=============================================================================================
try:
    l = 2 ** 1050
    print(l)
except OverflowError as lk: # OverflowError: Вызывается, когда результат арифметической операции слишком велик для представления.
    print(f"Result: {lk}")

#===========================================MemoryError=============================================================================================

try:
    lst = [0] * (10 * 8)
except MemoryError as w: # MemoryError: Вызывается, когда недостаточно памяти для выполнения операции.
    print(f"Error: Memory error {w}")

#============================================PermissionError============================================================================================
try:
    with open("bleach.txt", "w") as root_file:
        root_file.write("Bankai")
except PermissionError as r: # PermissionError: Вызывается, когда не хватает разрешений для выполнения операции с файлом или директорией.
    print(f"Error: {r}")

#=============================================TypeError===========================================================================================
try:
    zxc = "1" + 2
    print(zxc)
except TypeError as l: # TypeError: Вызывается, когда операция применяется к объекту несоответствующего типа.
    print(f"Error: {l}")

#=============================================NameError===========================================================================================

try:
    print(variable)
except NameError as v: # NameError: Вызывается, когда имя переменной не найдено в локальной или глобальной области видимости.
    print(f"Error: {v}")








#----------------------------------------------Rules------------------------------------------------------------------------

# ZeroDivisionError: Вызывается, когда происходит деление на ноль.
#
# TypeError: Вызывается, когда операция применяется к объекту несоответствующего типа.
#
# ValueError: Вызывается, когда функция получает аргумент правильного типа, но с недопустимым значением.
#
# IndexError: Вызывается, когда индекс последовательности находится за пределами допустимого диапазона.
#
# KeyError: Вызывается, когда ключ не найден в словаре.
#
# FileNotFoundError: Вызывается, когда файл или директория не найдены.
#
# ImportError: Вызывается, когда не удалось импортировать модуль или имя модуля не найдено.
#
# AttributeError: Вызывается, когда атрибут объекта не существует или не может быть использован.
#
# SyntaxError: Вызывается, когда обнаружена синтаксическая ошибка в коде.
#
# IndentationError: Вызывается, когда обнаружена ошибка в отступах.
#
# OverflowError: Вызывается, когда результат арифметической операции слишком велик для представления.
#
# MemoryError: Вызывается, когда недостаточно памяти для выполнения операции.
#
# PermissionError: Вызывается, когда не хватает разрешений для выполнения операции с файлом или директорией.
#
# TypeError: Вызывается, когда операция применяется к объекту несоответствующего типа.
#
# NameError: Вызывается, когда имя переменной не найдено в локальной или глобальной области видимости.








