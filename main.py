import tkinter as tk
from tkinter import ttk, messagebox
from fake_db import salvar_empresa

def tela_boas_vindas():
    global root
    root = tk.Tk()
    root.title("Bem-vindo ao Sistema")
    root.geometry("718x404")
    root.configure(bg="white")

    label_texto = tk.Label(root, text="Bem-vindo ao Cadastro de Empresas", font=("Arial", 14, "bold"), bg="white")
    label_texto.pack(pady=10)

    btn_iniciar = ttk.Button(root, text="Iniciar", command=abrir_tela_cadastro)
    btn_iniciar.pack(pady=20)

    root.mainloop()

def abrir_tela_cadastro():
    root.withdraw()
    tela_cadastro_empresas()

def cadastrar_empresa():
    razao_social = entry_razao_social.get()
    nome_fantasia = entry_nome_fantasia.get()
    cnpj = entry_cnpj.get()
    endereco = entry_endereco.get()
    cidade = entry_cidade.get()
    estado = entry_estado.get()
    cep = entry_cep.get()

    if all([razao_social, nome_fantasia, cnpj, endereco, cidade, estado, cep]):
        dados = {
            "razao_social": razao_social,
            "nome_fantasia": nome_fantasia,
            "cnpj": cnpj,
            "endereco": endereco,
            "cidade": cidade,
            "estado": estado,
            "cep": cep
        }
        salvar_empresa(dados)
        messagebox.showinfo("Sucesso", "Empresa cadastrada com sucesso!")
        for entry in [entry_razao_social, entry_nome_fantasia, entry_cnpj, entry_endereco, entry_cidade, entry_estado, entry_cep]:
            entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Preencha todos os campos.")

def tela_cadastro_empresas():
    app = tk.Toplevel()
    app.title("Cadastro de Empresas")
    app.geometry("420x550")
    app.configure(bg="#F0F0F0")

    ttk.Label(app, text="Cadastro de Empresas", font=("Arial", 14, "bold")).pack(pady=10)
    frame = tk.Frame(app, bg="white", padx=20, pady=20, relief="raised", bd=2)
    frame.pack(pady=20)

    fonte_label = ("Arial", 10, "bold")
    fonte_entry = ("Arial", 10)
    largura_entry = 35

    global entry_razao_social, entry_nome_fantasia, entry_cnpj
    global entry_endereco, entry_cidade, entry_estado, entry_cep

    ttk.Label(frame, text="Razão Social:", font=fonte_label).grid(row=0, column=0, sticky="w", pady=5)
    entry_razao_social = ttk.Entry(frame, font=fonte_entry, width=largura_entry)
    entry_razao_social.grid(row=0, column=1, pady=5)

    ttk.Label(frame, text="Nome Fantasia:", font=fonte_label).grid(row=1, column=0, sticky="w", pady=5)
    entry_nome_fantasia = ttk.Entry(frame, font=fonte_entry, width=largura_entry)
    entry_nome_fantasia.grid(row=1, column=1, pady=5)

    ttk.Label(frame, text="CNPJ:", font=fonte_label).grid(row=2, column=0, sticky="w", pady=5)
    entry_cnpj = ttk.Entry(frame, font=fonte_entry, width=largura_entry)
    entry_cnpj.grid(row=2, column=1, pady=5)

    ttk.Label(frame, text="Endereço:", font=fonte_label).grid(row=3, column=0, sticky="w", pady=5)
    entry_endereco = ttk.Entry(frame, font=fonte_entry, width=largura_entry)
    entry_endereco.grid(row=3, column=1, pady=5)

    ttk.Label(frame, text="Cidade:", font=fonte_label).grid(row=4, column=0, sticky="w", pady=5)
    entry_cidade = ttk.Entry(frame, font=fonte_entry, width=largura_entry)
    entry_cidade.grid(row=4, column=1, pady=5)

    ttk.Label(frame, text="Estado (UF):", font=fonte_label).grid(row=5, column=0, sticky="w", pady=5)
    entry_estado = ttk.Entry(frame, font=fonte_entry, width=5)
    entry_estado.grid(row=5, column=1, pady=5, sticky="w")

    ttk.Label(frame, text="CEP:", font=fonte_label).grid(row=6, column=0, sticky="w", pady=5)
    entry_cep = ttk.Entry(frame, font=fonte_entry, width=15)
    entry_cep.grid(row=6, column=1, pady=5, sticky="w")

    btn_cadastrar = ttk.Button(frame, text="Cadastrar", command=cadastrar_empresa)
    btn_cadastrar.grid(row=7, column=0, columnspan=2, pady=10)

tela_boas_vindas()
