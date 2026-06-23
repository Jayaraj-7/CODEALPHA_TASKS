import sqlite3
from cryptography.fernet import Fernet

# Generate key once and save securely
key = Fernet.generate_key()
cipher = Fernet(key)

# Create database
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    username TEXT,
    password BLOB
)
""")

# Store encrypted password
username = "admin"
password = "SecurePass123"

encrypted_password = cipher.encrypt(password.encode())

cursor.execute(
    "INSERT INTO users(username, password) VALUES (?, ?)",
    (username, encrypted_password)
)

conn.commit()

# Secure login check
user_input = "admin"
password_input = "SecurePass123"

cursor.execute(
    "SELECT password FROM users WHERE username=?",
    (user_input,)
)

record = cursor.fetchone()

if record:
    decrypted = cipher.decrypt(record[0]).decode()

    if decrypted == password_input:
        print("✅ Login Successful")
    else:
        print("❌ Invalid Password")
else:
    print("❌ User Not Found")

conn.close()