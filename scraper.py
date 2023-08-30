import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd
import array as arr
import numpy as np

'''
ID  CLASIFICACION OLIMPICA      CLASIFICACION JMM
1   ÁLGEBRA                     3-Polinomios, 4-Desigualdades, 5-Algebra
2   GEOMETRÍA                   2-Geometría
3   COMBINATORIA                6-Combinatoria
4   TEORÍA DE NÚMEROS           1-Teoría de números

ÁLGEBRA  -> 159  problemas
GEOMETRÍA -> 58  problemas
COMBINATORIA -> 38  problemas
TEORÍA DE NÚMEROS -> 129  problemas
'''

sn = 0
amount_problems = np.zeros((4,), dtype=int)

with open('problems-training.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Enunciado", "Category"])
    for i in range (1, 7):
        k = requests.get("https://wpd.ugr.es/~jmmanzano/preparacion/problemas.php?page=1&d=-1&c=" + str(i)).text
        soup = BeautifulSoup(k,'html.parser')
        page = int(int(soup.find("div", {"class": "paginador-boton-c"}).text.split()[-1][:-1])/5)
        for j in range(0, page+1):     
            k = requests.get("https://wpd.ugr.es/~jmmanzano/preparacion/problemas.php?page="+ str(5*j+1) +"&d=-1&c=" + str(i)).text
            soup = BeautifulSoup(k,'html.parser')
            for enunciado in soup.find_all("div", {"class": "enunciado"}):
                sn = sn + 1
                if i==1:
                    writer.writerow([sn, enunciado.text.rstrip().replace('\n', ' ').replace('\r', ''), 4])
                    amount_problems[3] = amount_problems[3] + 1
                if i==2:
                    writer.writerow([sn, enunciado.text.rstrip().replace('\n', ' ').replace('\r', ''), 2])
                    amount_problems[1] = amount_problems[1] + 1   
                if i==3 or i==4 or i==5:
                    writer.writerow([sn, enunciado.text.rstrip().replace('\n', ' ').replace('\r', ''), 1])
                    amount_problems[0] = amount_problems[0] + 1
                if i==6:
                    writer.writerow([sn, enunciado.text.rstrip().replace('\n', ' ').replace('\r', ''), 3])
                    amount_problems[2] = amount_problems[2] + 1

print("ÁLGEBRA  ->", amount_problems[0], " problemas")
print("GEOMETRÍA ->", amount_problems[1], " problemas")
print("COMBINATORIA ->", amount_problems[2], " problemas")
print("TEORÍA DE NÚMEROS ->", amount_problems[3], " problemas")