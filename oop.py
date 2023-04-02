# Task 1
# Decorator məntiqindən istifadə edərək hesablama kalkulyatoru

# def kalkulyatorr(func):
#     def wrapper(num1, num2):
#         a = func(num1, num2)
#         print("Cavab: ")
#         return a
#     return wrapper

# @kalkulyatorr
# def add(num1, num2):
#     return num1 + num2

# @kalkulyatorr
# def subtract(num1, num2):
#     return num1 - num2

# @kalkulyatorr
# def multiply(num1, num2):
#     return num1 * num2

# @kalkulyatorr
# def divide(num1, num2):
#     if num2 == 0:
#         return "Sıfıra bölünmə mümkün deyil!"
#     else:
#         return num1 / num2

# def get_numbers():
#     num1 = int(input("İlk rəqəm: "))
#     num2 = int(input("İkinci rəqəm: "))
#     return num1, num2

# print("Əməliyyatı seç:")
# print("1. Toplama")
# print("2. Çıxma")
# print("3. Vurma")
# print("4. Bölmə")

# secc = input("(1/2/3/4): ")

# num1, num2 = get_numbers()

# if secc == '1':
#     print(add(num1, num2))

# elif secc == '2':
#     print(subtract(num1, num2))

# elif secc == '3':
#     print(multiply(num1, num2))

# elif secc == '4':
#     print(divide(num1, num2))

# else:
#     print("Invalid input")


# Decorator məntiqindən istifadə edərək hesablama kalkulyatoru ---- --- --- bitdi


# Task 2:
# Seriallara aid console app-i inkişaf etdirmək. Sys argv və file məntiqlərini birləşdirəcəyik.

# import os
# import sys

# class addfilm:
#     def __init__(self):
#         self.salam = []

#     def eylansaxla(self):
#         name = input("Enter series name: ")
#         directorr = input("Enter director name: ")
#         numofseasons = input("Enter number of seasons: ")
#         numofepisodes = input("Enter number of episodes: ")
#         genre = input("Enter genre: ")
#         with open("main.txt", "a") as file:
#             file.write(f"\nSeries name : {name}\nCreated : {directorr}\nSeasons : {numofseasons}\nEpisodes : {numofepisodes}\nGenre : {genre}\n")
#         print("Added succesfully")

# if (sys.argv[1] == "add"):
#     elan = addfilm()
#     elan.eylansaxla()
# elif sys.argv[1] == "film" and sys.argv[2] == "sil":
#     try:
#         name = input("Silinəcək film adını daxil et: ")
#         os.remove(name)
#         print(f"{name} adli film silindi!")
#     except:
#         print("Belə not yoxdur!")

# elif sys.argv[1] == "all" and sys.argv[2] == "series":
#     file = open("main.txt", "r")
#     print("Not göstərildi")    
#     content = file.read()
#     print(content)
#     file.close()

# elif sys.argv[1] == "series" and sys.argv[2] == "delete":
#     f = open("main.txt", "r+")
#     f.seek(0)
#     f.truncate()