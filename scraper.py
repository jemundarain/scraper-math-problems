import requests
import csv
from bs4 import BeautifulSoup
import numpy as np

BASE_URL = "https://wpd.ugr.es/~jmmanzano/preparacion/problemas.php?page=1&d=-1&c="
sn = 0
amount_problems = np.zeros((4,), dtype=int)

def clean_text(text):
    return text.rstrip().replace('\n', ' ').replace('\r', '')

categories = [4, 2, 1, 1, 1, 3]

with open('problems-training.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Statement", "Category"])
    
    for i in range(1, 7):
        url = f"{BASE_URL}{i}"
        k = requests.get(url).text
        soup = BeautifulSoup(k, 'html.parser')
        page = int(soup.find("div", {"class": "paginador-boton-c"}).text.split()[-1][:-1]) // 5
        
        for j in range(page + 1):     
            url = f"{BASE_URL}{i}&page={5*j+1}"
            k = requests.get(url).text
            soup = BeautifulSoup(k, 'html.parser')
            
            for enunciado in soup.find_all("div", {"class": "enunciado"}):
                sn += 1
                category = categories[i - 1]
                writer.writerow([sn, clean_text(enunciado.text), category])
                amount_problems[category - 1] += 1

categories_names = ["ÁLGEBRA", "GEOMETRÍA", "COMBINATORIA", "TEORÍA DE NÚMEROS"]
for i in range(4):
    print(f"{categories_names[i]} -> {amount_problems[i]} problemas")

total_problems = sum(amount_problems)
print(f"Total de problemas -> {total_problems} problemas")
