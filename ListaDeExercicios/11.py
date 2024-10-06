from cryptography.fernet import Fernet

chave = Fernet.generate_key()
fernet = Fernet(chave)

arquivo = open('C:/arquivotexto.txt', 'w')
arquivo.write(chave.decode())
