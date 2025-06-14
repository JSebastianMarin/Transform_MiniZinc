import tkinter as tk
from tkinter import ttk, scrolledtext
from minizinc_code import generate_minizinc

example_text ="""12
5
Palmira 2 3
Cali 10 2
Buga 11 0
Tulua 0 3
RioFrio 1 2
"""

class ValleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Transformador a MiniZinc")
        self.root.geometry("1150x600")

        # Frame principal
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Área de texto para entrada
        ttk.Label(main_frame, text="Entrada:").grid(row=0, column=0, sticky=tk.W)
        self.input_text = scrolledtext.ScrolledText(main_frame, width=40, height=10)
        self.input_text.grid(row=1, column=0, padx=5, pady=5, sticky=tk.N)

        # Botón de solución
        self.solve_button = ttk.Button(main_frame, text="Generar MiniZinc", command=self.generate_minizinc)
        self.solve_button.grid(row=1, column=0, pady=10)

        # Área de texto para salida MiniZinc
        ttk.Label(main_frame, text="Código MiniZinc:").grid(row=0, column=2, sticky=tk.W)
        self.output_text = scrolledtext.ScrolledText(main_frame, width=90, height=30)
        self.output_text.grid(row=1, column=2, padx=5, pady=5)

        # Texto de ejemplo
        self.input_text.insert(tk.END, example_text)

    def generate_minizinc(self):
        try:
            # Obtener el texto de entrada
            input_data = self.input_text.get("1.0", tk.END).strip().split('\n')
            
            # Procesar la entrada
            N = int(input_data[0])
            M = int(input_data[1])
            ciudades = []
            
            # Validar que M coincida con el número de ciudades proporcionadas
            if len(input_data) - 2 != M:
                raise ValueError(f"El número de ciudades ({M}) no coincide con la cantidad de ciudades proporcionadas ({len(input_data)-2})")
            
            for i in range(2, 2 + M):
                nombre, x, y = input_data[i].split()
                ciudades.append((nombre, int(x), int(y)))
            
            # Generar código MiniZinc
            minizinc_code = generate_minizinc(N, M, ciudades)

            # Mostrar el código generado
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, minizinc_code)

        except Exception as e:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ValleApp(root)
    root.mainloop()
