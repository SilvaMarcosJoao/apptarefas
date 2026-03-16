import psycopg2

class Conexao:
    def __init__(self):
        self.db = "db_tarefas"
        self.user = "postgres"
        self.password = "1234"
        self.host = "localhost"

    def conectar(self):
        try:
            self.conecta = psycopg2.connect(
            database="db_tarefas",
            user=self.user,
            password=self.password,
            host=self.host  
            )
            self.conecta.autocommit = True
            self.cur = self.conecta.cursor()
        except (ConnectionError, psycopg2.DatabaseError) as e:
            print("Erro conectar-se ao banco", e)

    def desconectar(self):
        self.conecta.close()
        
    def criar_db(self):
        try:
            self.sql = f"CREATE DATABASE {self.db}" 
            self.cur.execute(self.sql)
        except psycopg2.errors.DuplicateDatabase:
            print("Este banco já existe")

    def criar_tabela_tarefa(self):
        
        self.query = """
            CREATE TABLE IF NOT EXISTS tarefa (
                id_tarefa SERIAL PRIMARY KEY,
                nome_tarefa VARCHAR(100) NOT NULL,
                descricao_tarefa VARCHAR(255) NOT NULL,
                status VARCHAR(100) not null check (status = 'Concluída' or status = 'Em Andamento' or status = 'Não Iniciada'),
                data_cadastro DATE,
                id_categoria integer not null references categoria
            )

        """
        self.conectar()
        self.cur.execute(self.query)
        self.conecta.commit()


    def criar_tabela_categoria(self):
        self.query = """
            CREATE TABLE IF NOT EXISTS categoria (
                id_categoria SERIAL PRIMARY KEY,
                nome_categoria VARCHAR(200) NOT NULL

            )

        """
        self.conectar()
        self.cur.execute(self.query)
        self.conecta.commit()



