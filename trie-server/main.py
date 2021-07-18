from fastapi import FastAPI
from .trie import Trie

trie = Trie()

app = FastAPI()



@app.get("/api")
def display():
    return trie

@app.get("/api/add/{keyword}")
def add(keyword: str):
    trie.add(keyword)
    return trie

@app.get("/api/search/{keyword}")
def search(keyword: str):
    return trie.search(keyword)

@app.get("/api/delete/{keyword}")
def delete(keyword: str):
    trie.delete(keyword)
    return trie

@app.get("/api/suggest/{keyword}")
def suggest(keyword: str):
    return trie.suggest(keyword)
