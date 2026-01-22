import pymysql

DB_NAME = "test"
def push_to_db():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor)
    
    cursor = conn.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    cursor.execute(f"USE {DB_NAME}")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS my_table (
            id INT AUTO_INCREMENT PRIMARY KEY,
            weapon_id VARCHAR(255),
            weapon_name VARCHAR(255),
            weapon_type VARCHAR(255),
            range_km INT,
            weight_kg FLOAT,
            manufacturer VARCHAR(255),
            origin_country VARCHAR(255),
            storage_location VARCHAR(255),
            year_estimated INT,
            level_risk VARCHAR(255)
        )""")
    conn.commit()
    return conn