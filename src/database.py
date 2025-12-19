from supabase import create_client
import os

def get_client():
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_KEY")

    if not url or not key:
        raise ValueError("Variáveis SUPABASE_URL e SUPABASE_KEY não estão configuradas.")

    return create_client(url, key)
