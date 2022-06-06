import random as rd
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
import time
import os

print(f"{Fore.RED}\t\t\t\t\tHoşgeldiniz")
print(f"{Fore.LIGHTYELLOW_EX}Oyunun amacı rastgele ekrana gelen harften iki önceki harfle aynı olup olmadığının hatırlanmasıdır. Bol şans")
print(f"{Fore.MAGENTA} - 0 = Doğru , 1 = Yanlış demektir.\n")
harfler = "AEGIJMX" #
liste_harf = []
liste_cevap = [0,0]
score = 0

dogru = 0
yanlis = 2
k = 0

for i in range(80):
    a = rd.choice(harfler)
    liste_harf.append(a)

while True:
    if k==78:
        break
    elif liste_harf[k] == liste_harf[k+2]:
        dogru += 1
        liste_cevap.append(1)
    else:
        yanlis += 1
        liste_cevap.append(0)
    k+=1

for i in range(len(liste_harf)):
    print(f"{Fore.BLUE}                    {i+1} / 80")
    x = input(f"{liste_harf[i]} : ")
    if x == str(liste_cevap[i]):
        print(f"Doğru Cevap ")
        score += 1
    else:
        print("Yanlis Cevap")
    time.sleep(0.7)
    os.system("clear")
print(f"\nPuanınız : {score}")

