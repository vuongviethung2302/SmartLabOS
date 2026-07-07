import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="smartlab_os",
        user="postgres",
        password="H23u02n88"
    )

    print("✅ psycopg2 kết nối thành công!")

    conn.close()

except Exception as e:
    print(e)