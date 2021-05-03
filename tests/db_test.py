import psycopg2

def postgres_test():

    try:
        conn = psycopg2.connect("dbname='test' user='prateek' host='127.0.0.1' password='prateek@123' connect_timeout=5 ")
        conn.close()
        return True
    except Exception as e: 
        print("Connection failed:", e)
        return False

print(postgres_test())