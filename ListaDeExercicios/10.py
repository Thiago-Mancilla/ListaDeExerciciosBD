from pymongo import MongoClient
from cryptography.fernet import Fernet

cliente = MongoClient("mongodb+srv://thiago:123@cluster0.bz0hk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cliente['BancoDeDados']
colecao = db['ListaDeExercicios']

msg_cript = colecao.find_one({'fernet_cript': { "$exists" : True }})
print(msg_cript)