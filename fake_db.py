import json
import os

ARQUIVO = "empresas.json"

def carregar_empresas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_empresa(empresa):
    empresas = carregar_empresas()
    empresas.append(empresa)
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(empresas, f, indent=4, ensure_ascii=False)
