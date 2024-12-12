from cryptography.fernet import Fernet

# Step 1: Generate a symmetric key
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Step 2: Original message
message = "Hello, this is a secret message!"
print(f"Original Message: {message}")

# Step 3: Encrypt the message
encrypted_message = cipher_suite.encrypt(message.encode())
print(f"Encrypted Message: {encrypted_message}")

# Step 4: Decrypt the message
decrypted_message = cipher_suite.decrypt(encrypted_message).decode()
print(f"Decrypted Message: {decrypted_message}")



output :
Original Message: Hello, this is a secret message!
Encrypted Message: b'gAAAAABlY...'
Decrypted Message: Hello, this is a secret message!
