import tkinter as tk
from tkinter import messagebox

# Função para calcular o IMC
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        imc = peso / (altura ** 2)
        resultado = f"Seu IMC é: {imc:.2f}"
        
        if imc < 18.5:
            resultado += "\nClassificação: Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            resultado += "\nClassificação: Peso normal"
        elif 25 <= imc < 29.9:
            resultado += "\nClassificação: Sobrepeso"
        else:
            resultado += "\nClassificação: Obesidade"
        
        messagebox.showinfo("Resultado", resultado)
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos para peso e altura.")

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de IMC")

# Criar e posicionar os widgets
label_peso = tk.Label(root, text="Peso (kg):")
label_peso.grid(row=0, column=0, padx=10, pady=10)

entry_peso = tk.Entry(root)
entry_peso.grid(row=0, column=1, padx=10, pady=10)

label_altura = tk.Label(root, text="Altura (m):")
label_altura.grid(row=1, column=0, padx=10, pady=10)

entry_altura = tk.Entry(root)
entry_altura.grid(row=1, column=1, padx=10, pady=10)

button_calcular = tk.Button(root, text="Calcular IMC", command=calcular_imc)
button_calcular.grid(row=2, column=0, columnspan=2, pady=10)

# Iniciar o loop principal da interface gráfica
root.mainloop()
