# Operações da tabela fornecedores
from database import get_client

# CRIANDO O ARQUIVO FORNECEDOR
from fastapi import APIRouter, HTTPException
from database import supabase

router = APIRouter(
    prefix="/fornecedores",
    tags=["Fornecedores"]
)

# CRIAR FORNECEDOR CREATE
@router.post("/")
def criar_fornecedor(dados: dict):
    response = supabase.table("fornecedores").insert(dados).execute()

    if not response.data:
        raise HTTPException(status_code=400, detail="Erro ao criar fornecedor")

    return response.data

# LISTAR TODOS FORNECEDORES (READ)
@router.get("/")
def listar_fornecedores():
    response = supabase.table("fornecedores").select("*").execute()
    return response.data

#BUSCAR FORNECEDOR POR ID
@router.get("/{fornecedor_id}")
def buscar_fornecedor(fornecedor_id: str):
    response = (
        supabase
        .table("fornecedores")
        .select("*")
        .eq("id", fornecedor_id)
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")

    return response.data[0]

#ATUALIZAR FORNECEDOR (UPDATE)
@router.put("/{fornecedor_id}")
def atualizar_fornecedor(fornecedor_id: str, dados: dict):
    response = (
        supabase
        .table("fornecedores")
        .update(dados)
        .eq("id", fornecedor_id)
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=400, detail="Erro ao atualizar fornecedor")

    return response.data

#EXCLUIR FORNECEDOR (DELETE)
@router.delete("/{fornecedor_id}")
def deletar_fornecedor(fornecedor_id: str):
    response = (
        supabase
        .table("fornecedores")
        .delete()
        .eq("id", fornecedor_id)
        .execute()
    )

    if not response.data:
        raise HTTPException(status_code=400, detail="Erro ao deletar fornecedor")

    return {"message": "Fornecedor removido com sucesso"}
