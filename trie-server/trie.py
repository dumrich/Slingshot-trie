
end_node = ""

class Trie:
    def __init__(self):
        self.root = dict()

    def add(self, keyword: str) -> dict:
        """Add value to trie"""
        dict_clone = self.root
        for char in keyword:
            dict_clone = dict_clone.setdefault(char, {})
        dict_clone[end_node] = end_node
        return self.root

    def search(self, keyword: str) -> bool:
        """Search for value in trie"""
        dict_clone = self.root
        for char in keyword:
            if char not in dict_clone:
                return False
            dict_clone = dict_clone[char]
        return end_node in dict_clone

    def delete(self, keyword: str) -> bool:
        """Search for value in trie"""
        dict_clone = self.root
        dict_clone.pop(keyword[0], None)
        return self.root

    def suggest(self, keyword: str):
        """Suggest value in trie"""
        dict_clone = self.root
        for char in keyword:
            if len(dict_clone) != 1:
                dict_clone = dict_clone[char]
            else: 
                return dict_clone

    def display(self):
        """Display trie"""
        return self.root

