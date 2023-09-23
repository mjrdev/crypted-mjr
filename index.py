from cryptography.fernet import Fernet

# Função para gerar uma chave de criptografia
def gen_keys():
    return Fernet.generate_key()

# Função para criptografar uma string com base em uma chave
def criptografar(chave, texto):
    cipher_suite = Fernet(chave)
    texto_bytes = texto.encode('utf-8')
    texto_criptografado = cipher_suite.encrypt(texto_bytes)
    return texto_criptografado

# Função para descriptografar uma string com base em uma chave
def descriptografar(chave, texto_criptografado):
    cipher_suite = Fernet(chave)
    texto_bytes = cipher_suite.decrypt(texto_criptografado)
    texto_descriptografado = texto_bytes.decode('utf-8')
    return texto_descriptografado

# Exemplo de uso
chave = gerar_chave()
texto_original = "Esta é uma mensagem secreta."

texto_criptografado = criptografar(chave, texto_original)
print("Texto criptografado:", texto_criptografado)

texto_descriptografado = descriptografar(chave, texto_criptografado)
print("Texto descriptografado:", texto_descriptografado)
