# Ponto inicial do sistema

def main():
    print("Sistema de Gestão de Cotações iniciado.")

if __name__ == "__main__":
    main()

#CONECTAR MÓDULO FORNECEDORES NO MAIN
from fastapi import FastAPI
from fornecedores import router as fornecedores_router

app = FastAPI()

app.include_router(fornecedores_router)

