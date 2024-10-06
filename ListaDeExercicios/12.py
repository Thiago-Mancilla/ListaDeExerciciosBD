from cryptography.fernet import Fernet

msg = input("Digite a mensagem que será criptografada: ")
arquivo = open('C:/arquivotexto.txt', 'r')
chave = arquivo.readline()
fernet = Fernet(chave)
msg_cript = fernet.encrypt(msg.encode())

print(f"Mensagem criptografada: {msg_cript.decode()}")
print(f'Chave utilizada: {chave}')