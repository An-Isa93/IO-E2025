import itertools
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from collections import Counter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Generar el espacio muestral de los dados
caras = range(1, 21)  # 20 caras en cada dado
espacio_muestral = list(itertools.product(caras, repeat=3))

# Calcular las sumas y frecuencias
x = [sum(espacio) for espacio in espacio_muestral]
frecuencia = Counter(x)

valores, frecuencias = zip(*sorted(frecuencia.items()))
ventana = tk.Tk()
ventana.title("Distribución de la Suma de 3 Dados de 20 Caras")
ventana.geometry("1080x600")

# Crear figura de Matplotlib
fig, axs = plt.subplots(figsize=(8, 5))
axs.bar(valores, frecuencias, color='purple')
axs.set_xlabel("Valor de X (Suma de los 3 dados)")
axs.set_ylabel("Frecuencia")
axs.set_title("Distribución de la Suma de 3 Dados de 20 Caras")

# Incrustar la gráfica en la ventana de Tkinter
canvas = FigureCanvasTkAgg(fig, master=ventana)
canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
canvas.draw()

# Crear un frame para la tabla
table = tk.Frame(ventana)
table.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

  
scrollbar_y = tk.Scrollbar(table, orient=tk.VERTICAL)

    
#Crear tabla con Treeview
tabla = ttk.Treeview(table, columns=("Dado 1", "Dado 2", "Dado 3", "Suma"),
                          show="headings", yscrollcommand=scrollbar_y.set)
    
for col in ("Dado 1", "Dado 2", "Dado 3", "Suma"):
        tabla.heading(col, text=col)
        tabla.column(col, width=50, anchor="center")
    
# Espacio muestral de los 3 dados asi como su respectiva suma
for espacio in espacio_muestral[:8000]: 
        tabla.insert("", "end", values=(*espacio, sum(espacio)))
    
scrollbar_y.config(command=tabla.yview)
   
tabla.grid(row=0, column=0, sticky="nsew")  
scrollbar_y.grid(row=0, column=1, sticky="ns")  # Scrollbar vertical a la derecha

    
table.grid_rowconfigure(0, weight=1)
table.grid_columnconfigure(0, weight=1)
    
ventana.mainloop()


