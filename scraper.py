import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import array as arr
import numpy as np

'''
ID  CLASIFICACION OLIMPICA      CLASIFICACION JMM
1   ÁLGEBRA                     3-Polinomios, 4-Desigualdades, 5-Ecuaciones funcionales, 9-Sucesiones y series
2   GEOMETRÍA                   2-Geometría
3   PROBABILIDAD                6-Combinatoria
4   TEORÍA DE NÚMEROS           1-Teoría de números
'''

sn = 0
count_prob = np.zeros((4,), dtype=int)

with open('problems-training.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Enunciado", "Category"])
    for i in range (1, 10):
        if i!=7 and i!=8:
            k = requests.get("https://wpd.ugr.es/~jmmanzano/preparacion/problemas.php?page=1&d=-1&c=" + str(i)).text
            soup = BeautifulSoup(k,'html.parser')
            page = int(int(soup.find("div", {"class": "paginador-boton-c"}).text.split()[-1][:-1])/5)
            for j in range(0, page+1):     
                k = requests.get("https://wpd.ugr.es/~jmmanzano/preparacion/problemas.php?page="+ str(5*j+1) +"&d=-1&c=" + str(i)).text
                soup = BeautifulSoup(k,'html.parser')
                for enunciado in soup.find_all("div", {"class": "enunciado"}):
                    sn = sn + 1
                    if i==1:
                        writer.writerow([sn, enunciado.text, 4])
                        count_prob[3] = count_prob[3] + 1
                    if i==2:
                        writer.writerow([sn, enunciado.text, 2])
                        count_prob[1] = count_prob[1] + 1   
                    if i==3 or i==4 or i==5 or i==9:
                        writer.writerow([sn, enunciado.text, 1])
                        count_prob[0] = count_prob[0] + 1
                    if i==6:
                        writer.writerow([sn, enunciado.text, 3])
                        count_prob[2] = count_prob[2] + 1

print("ÁLGEBRA  ->", count_prob[0], " problemas")
print("GEOMETRÍA ->", count_prob[1], " problemas")
print("PROBABILIDAD ->", count_prob[2], " problemas")
print("TEORÍA DE NÚMEROS ->", count_prob[3], " problemas")