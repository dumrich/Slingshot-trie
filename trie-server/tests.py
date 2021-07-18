from trie import Trie

trie = Trie()

def test_trie_insert_keyword(keyword):
    return trie.add(keyword)

def test_trie_search_keword(keyword):
    return trie.search(keyword)

def test_trie_delete_keyword(keyword):
    return trie.delete(keyword)

def test_trie_suggest_keyword(keyword):
    return trie.suggest(keyword)

def test_trie_display_keyword():
    return trie.display()

print(test_trie_insert_keyword("hello"))
print(test_trie_insert_keyword("goodbye"))
print(test_trie_insert_keyword("goodbye"))
print(test_trie_delete_keyword("goodbye"))
print(test_trie_suggest_keyword("hell"))
print(test_trie_display_keyword())
