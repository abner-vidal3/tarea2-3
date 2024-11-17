import subprocess
import psutil
import time
import csv

def ejecutar_binario(binario, archivo_entrada):
    start_time = time.time()  
    process = subprocess.Popen([binario], stdin=open(archivo_entrada, 'r'), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    pid = process.pid
    proc = psutil.Process(pid)
    max_memoria = 0  
    while process.poll() is None:
        elapsed_time = time.time() - start_time
        if elapsed_time > 120:
            process.terminate() 
            return -1, -1 
        memoria = proc.memory_info().rss / (1024 * 1024)
        max_memoria = max(max_memoria, memoria)
        time.sleep(0.1) 
    process.wait()  
    end_time = time.time()
    total_time = end_time - start_time
    return total_time, max_memoria
col1 = []
col2 = []
for i in range(17):
    binario = "./a"
    archivo_entrada = "tests/"+str(i)+".txt" 
    print(i)
    tiempo, memoria = ejecutar_binario(binario, archivo_entrada)
    col1.append(tiempo)
    col2.append(memoria)
tipo_caso = []
for i in range(5):
    tipo_caso.append(0)
for i in range(5):
    tipo_caso.append(1)
for i in range(3):
    tipo_caso.append(2)
for i in range(4):
    tipo_caso.append(3)
for i in range(3):
    tipo_caso.append(4)
for i in range(3):
    tipo_caso.append(5)
nombre_archivo = "resultadosbrute.csv"
numeros_de_caso = 17
with open(nombre_archivo, mode='w', newline='') as archivo:
    writer = csv.writer(archivo)
    writer.writerow(["Número de Caso", "Tipo Caso", "Tiempo (segundos)", "Memoria (MB)"])
    for i in range(numeros_de_caso):
        writer.writerow([i+1,tipo_caso[i], col1[i], col2[i]])
print(f"Archivo {nombre_archivo} generado exitosamente.")
