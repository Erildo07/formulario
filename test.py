import tkinter as tk
from tkinter import messagebox

# Criar a janela principal
root = tk.Tk()
root.title("Formulário de Cadastro")

# Dados Pessoais
tk.Label(root, text="Nome Completo:").grid(row=0, column=0)
entry_nome = tk.Entry(root)
entry_nome.grid(row=0, column=1)

tk.Label(root, text="Data de Nascimento:").grid(row=1, column=0)
entry_data_nascimento = tk.Entry(root)
entry_data_nascimento.grid(row=1, column=1)

tk.Label(root, text="Gênero:").grid(row=2, column=0)
var_genero = tk.StringVar(value="Masculino")
tk.Radiobutton(root, text="Masculino", variable=var_genero, value="Masculino").grid(row=2, column=1, sticky="w")
tk.Radiobutton(root, text="Feminino", variable=var_genero, value="Feminino").grid(row=2, column=2, sticky="w")
tk.Radiobutton(root, text="Outro", variable=var_genero, value="Outro").grid(row=2, column=3, sticky="w")

# Informações de Contato
tk.Label(root, text="E-mail:").grid(row=3, column=0)
entry_email = tk.Entry(root)
entry_email.grid(row=3, column=1)

tk.Label(root, text="Telefone:").grid(row=4, column=0)
entry_telefone = tk.Entry(root)
entry_telefone.grid(row=4, column=1)

# Endereço
tk.Label(root, text="Rua:").grid(row=5, column=0)
entry_rua = tk.Entry(root)
entry_rua.grid(row=5, column=1)

tk.Label(root, text="Número:").grid(row=6, column=0)
entry_numero = tk.Entry(root)
entry_numero.grid(row=6, column=1)

tk.Label(root, text="Bairro:").grid(row=7, column=0)
entry_bairro = tk.Entry(root)
entry_bairro.grid(row=7, column=1)

tk.Label(root, text="Cidade:").grid(row=8, column=0)
entry_cidade = tk.Entry(root)
entry_cidade.grid(row=8, column=1)

tk.Label(root, text="Estado:").grid(row=9, column=0)
entry_estado = tk.Entry(root)
entry_estado.grid(row=9, column=1)

tk.Label(root, text="CEP:").grid(row=10, column=0)
entry_cep = tk.Entry(root)
entry_cep.grid(row=10, column=1)

# Interesses
tk.Label(root, text="Interesses:").grid(row=11, column=0)
interesses_var = {
    "Tecnologia": tk.BooleanVar(),
    "Saúde": tk.BooleanVar(),
    "Esportes": tk.BooleanVar(),
    "Cultura": tk.BooleanVar(),
}
for i, interesse in enumerate(interesses_var):
    tk.Checkbutton(root, text=interesse, variable=interesses_var[interesse]).grid(row=11+i, column=1, sticky="w")

# Botão de enviar
btn_submit = tk.Button(root, text="Enviar")

# Comportamento ao clicar no botão
def on_submit():
    nome = entry_nome.get()
    data_nascimento = entry_data_nascimento.get()
    genero = var_genero.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    rua = entry_rua.get()
    numero = entry_numero.get()
    bairro = entry_bairro.get()
    cidade = entry_cidade.get()
    estado = entry_estado.get()
    cep = entry_cep.get()
    interesses = [interest for interest in interesses_var if interesses_var[interest].get()]
    
    print(f"Nome: {nome}")
    print(f"Data de Nascimento: {data_nascimento}")
    print(f"Gênero: {genero}")
    print(f"E-mail: {email}")
    print(f"Telefone: {telefone}")
    print(f"Endereço: {rua}, {numero}, {bairro}, {cidade}, {estado}, {cep}")
    print(f"Interesses: {', '.join(interesses)}")
    
    messagebox.showinfo("Formulário Enviado", "Dados enviados com sucesso!")

btn_submit.config(command=on_submit)
btn_submit.grid(row=15, column=1)

# Iniciar o loop da interface
root.mainloop()

