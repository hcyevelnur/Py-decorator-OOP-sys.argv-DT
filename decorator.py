        # t a s k - - - - - - 1

# import sys
# import os

# if (sys.argv[1] == "create" and sys.argv[2] == "folder"):
#     try:
#         directory = input("Qovluq adını qeyd et: ") 
#         parent_dir = "/Users/hcyevelnur/Desktop/backend/day-1-decerator"
#         path = os.path.join(parent_dir, directory) 
#         os.mkdir(path)
#         print(directory + ": adlı qovluqunuz yaradıldı.")
#     except:
#         print("Bu adli fayl var!")

# elif (sys.argv[1] == "remove" and sys.argv[2] == "folder"):
#     try:
#         directory = input("Qovluq adını qeyd et: ") 
#         parent_dir = "/Users/hcyevelnur/Desktop/backend/day-1-decerator"
#         path = os.path.join(parent_dir, directory) 
#         os.rmdir(path)
#         print(directory + ": adlı qovluqunuz silindi.")
#     except:
#         print("Bu adli fayl yoxdur!")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # t a s k - - - - - - 2

# import sys
# from datetime import datetime

# if len(sys.argv) > 1 and sys.argv[1] == 'show' and sys.argv[2] == 'my' and sys.argv[3] == 'age' and sys.argv[4] == 'information':
#     print("Ad gününüzü qeyd edin.(Məsələn: 01-01-2000):")

# adgunugirr = input()
# adgunu = datetime.strptime(adgunugirr, "%d-%m-%Y")

# bugun = datetime.now()
# sonraki_adgunu = datetime(bugun.year, adgunu.month, adgunu.day)

# if bugun > sonraki_adgunu:
#     sonraki_adgunu = sonraki_adgunu.replace(year=bugun.year + 1)

# age = bugun.year - adgunu.year
# if bugun < sonraki_adgunu:
#     age -= 1

# print(f'{age} yaşınız var.')
# print("Sonrakı ad gününüz:", sonraki_adgunu.strftime("%A, %B %d, %Y"))
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

        # t a s k - - - - - - 3

# import sys

# filmler_1 = [
#     'Created - Vince Gilligan',
#     'Series name - Breaking Bad',
#     'Genre - Crime Drama',
#     'Episodes - 62',
#     'Release - 20 Yanvar 2008',
#     'Seasons - 5']

# filmler_2 = [
#     'Created - Jantje Friese',
#     'Series name - Dark',
#     'Genre - Science fiction',
#     'Episodes - 26',
#     'Release - 01 December 2017',
#     'Seasons - 3']


# filmler_3 = [
#     'Created - Robert Krikman',
#     'Series name - The Walking Dead',
#     'Genre - Horror',
#     'Episodes - 153',
#     'Release - 31 October 2010',
#     'Seasons - 10']

# if len(sys.argv) < 4:
#     print('Wrong input')
# elif sys.argv[1] == "Breaking" and sys.argv[2] == "Bad" and sys.argv[3] == "-" and sys.argv[4] == "Vince" and sys.argv[5] == "Gilligan":
#     for a in filmler_1:
#         print(a) 
# elif sys.argv[1] == "The" and sys.argv[2] == "Walking" and sys.argv[3] == "Dead":
#     for c in filmler_3:
#         print(c) 
# elif sys.argv[1] == "Dark" and sys.argv[2] == "Jantje" and sys.argv[3] == "Friese":
#     for b in filmler_2:
#         print(b) 
# else:
#     print('Wrong input')





