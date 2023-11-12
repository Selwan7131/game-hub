class TrieNode:
    def __init__(self):
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.node = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.node
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]


    def search(self, word: str, curNode=None) -> bool:
        cur = self.node
        if curNode:
            cur = curNode
        for i in range(len(word)):
            if word[i] == '.':
                for child in cur.children.values():
                    return self.search(word[i+1:], child)
            elif word[i] not in cur.children:
                return False
            cur = cur.children[word[i]]
        return True

obj = WordDictionary()
obj.addWord("a")
obj.addWord("a")
param_2 = obj.search(".")
param_2 = obj.search("a")
param_3 = obj.search("aa")
param_4 = obj.search("a.")
param_5 = obj.search(".a")