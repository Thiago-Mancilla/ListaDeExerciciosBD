from pymongo import MongoClient
import hashlib

cliente = MongoClient("mongodb+srv://thiago:123@cluster0.bz0hk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = cliente['BancoDeDados']
colecao = db['ListaDeExercicios']

texto = input("Digite sua string: ")
stringhash = hashlib.sha256(texto.encode()).hexdigest()
if colecao.find_one({'hash_cript' : stringhash}):
    print("Hash já presente no banco!")
else:
    print("Hash ainda não presente no banco!")
