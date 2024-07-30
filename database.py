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
    cur.execute('''CREATE TABLE IF NOT EXISTS history
                (
                equation VARCHAR(100)
                );
                ''')
    connection.commit()
    cur.close()
    return connection
    
def insert_data(connection, equation):
    try:
        cursor = connection.cursor()
        insert_data_query = '''INSERT INTO history (equation) VALUES (%s)'''
        cursor.execute(insert_data_query, (equation,))  # Correctly pass the equation parameter as a tuple
        connection.commit()
    except Exception as error:
        print(f"Error: {error}")
    finally:
        cursor.close()

def fetch_data(connection):
    try: 
        cursor = connection.cursor()
        cursor.execute('''SELECT * FROM history LIMIT 20''')
        data = cursor.fetchall()
        return data
    except Exception as error:
        print(f"Error: {error}")
    finally:
        cursor.close()
    

    

