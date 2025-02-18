import sqlite3

def execute_sql_from_file(db_name, sql_file_path):
    # Conectar ao banco de dados SQLite
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Abrir o arquivo .sql e ler o conteúdo
    with open(sql_file_path, 'r') as file:
        sql_script = file.read()
    
    # Executar o script SQL
    cursor.executescript(sql_script)
    
    # Commit e fechar conexão
    conn.commit()
    conn.close()

def seed_database():
    # Caminho para o arquivo SQL
    sql_file_path = '/home/caio/github-repositories/pessoal/dev-stage/python/db/schema.sql'  # Substitua pelo caminho real do seu arquivo .sql
    db_name = '/home/caio/github-repositories/pessoal/dev-stage/python/db/schema.db'  # Nome do seu banco de dados SQLite
    
    # Executar o seed
    execute_sql_from_file(db_name, sql_file_path)
    print(f"Seed executado com sucesso no banco de dados {db_name}")

if __name__ == "__main__":
    seed_database()
