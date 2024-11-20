import subprocess
import psutil
import time
import csv

import subprocess
import time
import psutil
import os
def ejecutar_binario(binario, archivo_entrada):
    start_time = time.time()
    try:
        process = subprocess.Popen(
            [binario],
            stdin=open(archivo_entrada, 'r'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        pid = process.pid
        proc = psutil.Process(pid)
        max_memoria = 0 
        while process.poll() is None:  
            elapsed_time = time.time() - start_time
            if elapsed_time > 5: 
                process.terminate()
                return -1, -1
            memoria = proc.memory_info().rss / (1024 * 1024)  
            max_memoria = max(max_memoria, memoria)
            time.sleep(0.1) 
        process.wait()
        end_time = time.time()
        total_time = end_time - start_time
        if process.returncode == 139: 
            return -1, -1 
        elif process.returncode != 0:
            return -1, -1
        return total_time, max_memoria
    except Exception as e:
        return -1, -1
data_run = []
bin1 = "./a"
bin2 = "./b"
for i in range(80):
    archivo_entrada = "tests/"+str(i)+".txt" 
    print(i)
    t1, m1 = ejecutar_binario(bin1, archivo_entrada)
    t2, m2 = ejecutar_binario(bin2, archivo_entrada)
    info_run = [t1,m1,t2,m2]
    data_run.append(info_run)
data_case = [[0, 0, 2], [1, 0, 3], [2, 0, 4], [3, 0, 5], [4, 0, 6], [5, 0, 11], [6, 0, 21], [7, 0, 31], [8, 0, 41], [9, 0, 51], [10, 0, 101], [11, 0, 201], [12, 0, 301], [13, 0, 401], [14, 0, 501], [15, 0, 1001], [16, 0, 2001], [17, 0, 3001], [18, 0, 4001], [19, 0, 5001], [20, 1, 4], [21, 1, 9], [22, 1, 16], [23, 1, 25], [24, 1, 36], [25, 1, 121], [26, 1, 441], [27, 1, 961], [28, 1, 1681], [29, 1, 2601], [30, 1, 10201], [31, 1, 40401], [32, 1, 90601], [33, 1, 160801], [34, 1, 251001], [35, 1, 1002001], [36, 1, 4004001], [37, 1, 9006001], [38, 1, 16008001], [39, 1, 25010001], [40, 2, 2], [41, 2, 6], [42, 2, 16], [43, 2, 15], [44, 2, 18], [45, 2, 66], [46, 2, 252], [47, 2, 589], [48, 2, 1148], [49, 2, 1581], [50, 2, 6666], [51, 2, 25527], [52, 2, 61705], [53, 2, 104661], [54, 2, 166833], [55, 2, 664664], [56, 2, 2579289], [57, 2, 5881960], [58, 2, 10810702], [59, 2, 16288257], [60, 3, 8], [61, 3, 42], [62, 3, 32], [63, 3, 48], [64, 3, 60], [65, 3, 121], [66, 3, 575], [67, 3, 1120], [68, 3, 1892], [69, 3, 2860], [70, 3, 10815], [71, 3, 41410], [72, 3, 93025], [73, 3, 162810], [74, 3, 253512], [75, 3, 1012036], [76, 3, 4018018], [77, 3, 9012003], [78, 3, 16028012], [79, 3, 25055030]]
nombre_archivo = "resultados.csv"
with open(nombre_archivo, mode='w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Número de Caso", "Tipo Caso", "Tamaño input", "Tiempo (segundos) DP", "Memoria (MB) DP","Tiempo (segundos) Brute", "Memoria (MB) Br" ])
    for i in range(80):
        writer.writerow([data_case[i][0]+1,data_case[i][1],data_case[i][2], data_run[i][0], data_run[i][1],data_run[i][2],data_run[i][3]])
print(f"Archivo {nombre_archivo} generado exitosamente.")
