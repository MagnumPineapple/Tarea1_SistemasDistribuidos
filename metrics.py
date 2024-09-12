import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk


# Datos para LRU
data_lru = {
    'Escenario': ['Escenario 1 (Única)', 'Escenario 2 (2 Particiones)', 'Escenario 2 (4 Particiones)', 'Escenario 2 (8 Particiones)', 'Escenario 3 (2 Particiones)', 'Escenario 3 (4 Particiones)', 'Escenario 3 (8 Particiones)'],
    'Hit Rate (%)': [100.00, 0.00, 0.00, 0.00, 42.23, 60.61, 83.06],
    'Misses': [0, 10000, 10000, 10000, 5777, 3939, 1694],
    'Promedio Tiempo Respuesta (s)': [0.0088, 0.9128, 0.0091, 0.0090, 0.5050, 0.3484, 0.1249],
    'Desviación Estándar Tiempo (s)': [0.0040, 3.2020, 0.0041, 0.0038, 2.3610, 2.0780, 1.1893]
}

# Datos para LFU
data_lfu = {
    'Escenario': ['Escenario 1 (Única)', 'Escenario 2 (2 Particiones)', 'Escenario 2 (4 Particiones)', 'Escenario 2 (8 Particiones)', 'Escenario 3 (2 Particiones)', 'Escenario 3 (4 Particiones)', 'Escenario 3 (8 Particiones)'],
    'Hit Rate (%)': [0.00, 49.08, 49.83, 100.00, 79.07, 91.37, 100.00],
    'Misses': [10000, 5092, 5017, 0, 2093, 863, 0],
    'Promedio Tiempo Respuesta (s)': [0.0091, 0.3885, 0.4648, 0.0089, 0.2197, 0.0750, 0.0089],
    'Desviación Estándar Tiempo (s)': [0.0041, 2.1258, 2.2999, 0.0038, 1.7957, 1.1074, 0.0038]
}


df_lru = pd.DataFrame(data_lru)
df_lfu = pd.DataFrame(data_lfu)


def mostrar_metricas(df, title):
    print(f"\n{title}")
    print(df.to_string(index=False))

def mostrar_en_ventana(df_lru, df_lfu):
    root = tk.Tk()
    root.title("Resultados Comparativos - LRU y LFU")

  
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Pestaña para LRU
    lru_frame = ttk.Frame(notebook)
    notebook.add(lru_frame, text='LRU')

    # Pestaña para LFU
    lfu_frame = ttk.Frame(notebook)
    notebook.add(lfu_frame, text='LFU')

    
    def mostrar_tabla(df, frame):
        table = ttk.Treeview(frame, columns=list(df.columns), show='headings')
        table.pack(fill='both', expand=True)

        
        for col in df.columns:
            table.heading(col, text=col)

        # Agregar los datos
        for index, row in df.iterrows():
            table.insert("", "end", values=list(row))

    
    mostrar_tabla(df_lru, lru_frame)
    mostrar_tabla(df_lfu, lfu_frame)

    root.mainloop()


mostrar_metricas(df_lru, "Métricas Comparativas - LRU")
mostrar_metricas(df_lfu, "Métricas Comparativas - LFU")

def mostrar_resultados_por_escenario():
    
    print("\nEscenario 1 - Resultados:")
    print(df_lru.iloc[0:1])
    print(df_lfu.iloc[0:1])

    print("\nEscenario 2 - Resultados:")
    print(df_lru.iloc[1:4])
    print(df_lfu.iloc[1:4])

    print("\nEscenario 3 - Resultados:")
    print(df_lru.iloc[4:])
    print(df_lfu.iloc[4:])

def plot_hit_rate():
    plt.figure(figsize=(10, 6))
    plt.plot(df_lru['Escenario'], df_lru['Hit Rate (%)'], label='LRU', marker='o')
    plt.plot(df_lfu['Escenario'], df_lfu['Hit Rate (%)'], label='LFU', marker='o')
    plt.title('Hit Rate Comparativo LRU vs LFU')
    plt.xlabel('Escenario')
    plt.ylabel('Hit Rate (%)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_response_time():
    plt.figure(figsize=(10, 6))
    plt.plot(df_lru['Escenario'], df_lru['Promedio Tiempo Respuesta (s)'], label='LRU', marker='o')
    plt.plot(df_lfu['Escenario'], df_lfu['Promedio Tiempo Respuesta (s)'], label='LFU', marker='o')
    plt.title('Tiempo de Respuesta Comparativo LRU vs LFU')
    plt.xlabel('Escenario')
    plt.ylabel('Promedio Tiempo Respuesta (s)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_response_time_std():
    plt.figure(figsize=(10, 6))
    plt.plot(df_lru['Escenario'], df_lru['Desviación Estándar Tiempo (s)'], label='LRU', marker='o')
    plt.plot(df_lfu['Escenario'], df_lfu['Desviación Estándar Tiempo (s)'], label='LFU', marker='o')
    plt.title('Desviación Estándar de Tiempo de Respuesta LRU vs LFU')
    plt.xlabel('Escenario')
    plt.ylabel('Desviación Estándar Tiempo (s)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_hit_rate()
plot_response_time()
plot_response_time_std()

mostrar_en_ventana(df_lru, df_lfu)

mostrar_resultados_por_escenario()
