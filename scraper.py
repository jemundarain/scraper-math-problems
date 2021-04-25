import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

# 1 Teoría de números
# 2 Geometría
# 3 Polinomios
# 4 Desigualdades X
# 5 Ecuaciones funcionales
# 6 Combinatoriacls
# 7 Juegos y estrategia
# 8 Números y funciones
# 9 Sucesiones y series

# 1 - Aritmética 
# 2 - Álgebra
# 3 - Geometría 
# 4 - Combinatoria 
# 5 - Sucesiones y series 
# 6 - Juegos de estrategia 
# 7 - Polinomios y ecuaciones 
# 8 - Lógica
# 9 - Razonamiento en 2D
# 10 - Razonamiento en 3D

sn = 0
with open('problems-training.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Enunciado", "Category"])
    for i in range (1, 10):
        if i!=4:
            k = requests.get("https://wpd.ugr.es/~jmmanzano/preparacion/problemas.php?page=1&d=-1&c=" + str(i)).text
            soup = BeautifulSoup(k,'html.parser')
            page = int(int(soup.find("div", {"class": "paginador-boton-c"}).text.split()[-1][:-1])/5)
            for j in range(0, page+1):     
                k = requests.get("https://wpd.ugr.es/~jmmanzano/preparacion/problemas.php?page="+ str(5*j+1) +"&d=-1&c=" + str(i)).text
                soup = BeautifulSoup(k,'html.parser')
                for enunciado in soup.find_all("div", {"class": "enunciado"}):
                    sn = sn + 1
                    if i==1:
                        writer.writerow([sn, enunciado.text, 1])
                    if i==2:
                        writer.writerow([sn, enunciado.text, 3])
                    if i==3 or i==5:
                        writer.writerow([sn, enunciado.text, 7])
                    if i==6:
                        writer.writerow([sn, enunciado.text, 4])
                    if i==7:    
                        writer.writerow([sn, enunciado.text, 6])
                    if i==8:
                        writer.writerow([sn, enunciado.text, 2])
                    if i==9:
                        writer.writerow([sn, enunciado.text, 5])