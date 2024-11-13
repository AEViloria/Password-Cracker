import hashlib

# Cargar las contraseñas comunes desde el archivo
def load_passwords():
    with open('top-10000-passwords.txt', 'r') as file:
        passwords = [line.strip() for line in file]
    return passwords

# Cargar los salts conocidos desde el archivo
def load_salts():
    with open('known-salts.txt', 'r') as file:
        salts = [line.strip() for line in file]
    return salts

# Función para calcular el hash SHA-1 de un texto dado
def sha1_hash(text):
    return hashlib.sha1(text.encode()).hexdigest()

# Función principal para descifrar la contraseña
def crack_password(sha1_hash, use_salts=False):
    passwords = load_passwords()
    salts = load_salts() if use_salts else []

    # Verificar cada contraseña sin salts
    for password in passwords:
        if sha1_hash == sha1_hash(password):
            return password
    
    # Verificar cada contraseña con salts
    if use_salts:
        for password in passwords:
            for salt in salts:
                # Probar el hash con el salt antes y después de la contraseña
                if sha1_hash == sha1_hash(salt + password):
                    return password
                if sha1_hash == sha1_hash(password + salt):
                    return password
    
    return "PASSWORD NOT IN DATABASE"
