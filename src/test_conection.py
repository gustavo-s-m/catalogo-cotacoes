from database import supabase

def main():
    response = supabase.table("fornecedores").select("*").execute()
    print(response)

if __name__ == "__main__":
    main()