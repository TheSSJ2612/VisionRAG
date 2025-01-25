import psycopg

try:
    conn = psycopg.connect("postgresql://aivision:password@localhost:5432/maindb")
    print("Connection successful!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {str(e)}")
