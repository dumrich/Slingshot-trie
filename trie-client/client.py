import requests
import argparse

parser = argparse.ArgumentParser(description="Slingshot trie client, in Python")
parser.add_argument('--keyword', type=str, help="keyword to perform function on")
args = parser.parse_args()

method = input("Enter the function you would like to perform: ")

def get(method: str, keyword: str) -> str:
    """Get endpoint"""
    if method=="display":
        r = requests.get(f'https://slingshot-trie.herokuapp.com/api/')
    else:
        r = requests.get(f'https://slingshot-trie.herokuapp.com/api/{method}/{keyword}/')
    return r.json()

if __name__=="__main__":
    print(get(method, args.keyword))
