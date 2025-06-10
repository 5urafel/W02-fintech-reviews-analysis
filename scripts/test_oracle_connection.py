import oracledb

try:
    connection = oracledb.connect(
        user="system",
        password="Ora@5540sura",  # Replace with your Oracle XE password
        dsn="localhost:1521/XE"
    )
    print("Successfully connected to Oracle XE")
    connection.close()
except oracledb.Error as e:
    print(f"Connection failed: {e}")