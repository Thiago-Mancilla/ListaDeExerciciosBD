from pymongo import MongoClient
from cryptography.fernet import Fernet

cliente = MongoClient("mongodb+srv://thiago:123@cluster0.bz0hk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cliente['BancoDeDados']
colecao = db['ListaDeExercicios']

msg = input("Digite sua mensagem:")
chave = Fernet.generate_key()
fernet = Fernet(chave)
msg_cript = fernet.encrypt(msg.encode())

colecao.insert_one({'fernet_descript' : msg, 'fernet_cript' : msg_cript})