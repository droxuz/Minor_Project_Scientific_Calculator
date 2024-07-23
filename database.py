import psycopg2
#Example parameters for PostgresSQL connection
hostname = 'localhost'
database = 'Minor_Calculator'
username = 'postgres'
password = '5qff849g' 
port = '5432'

#Connects database and stores abitrary values
def create_database():
    try:
        connection = psycopg2.connect(host = hostname, dbname = database, user = username, password = password, port=port)
    except Exception as error:
        print(f"Error: {error}")
    cur = connection.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS person 
                (
                id INT PRIMARY KEY,
                equation VARCHAR(255)
                )
                ''')
    cur.execute(""" INSERT INTO person (id ,equation) VALUES
                (1, '(2+2)/3'),
                (2, '(2+2)/3'),
                (3, '(2+2)/3'),
                (4, '(2+2)/3');
                """)
    connection.commit()

