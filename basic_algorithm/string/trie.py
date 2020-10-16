class TrieNode:

    # Trie node class
    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Trie:

    # Trie data structure class
    def __init__(self):
        self.root = self.getNode()

    def getNode(self):

        # Returns new trie node (initialized to NULLs)
        return TrieNode()

    def _charToIndex(self, ch):

        # private helper function
        # Converts key current character into index
        # use only 'a' through 'z' and lower case
        # translate
        return ord(ch) - ord('a')

    def insert(self, key):

        # If not present, inserts key into trie
        # If the key is prefix of trie node,
        # just marks leaf node
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            # if current character is not present
            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

            # mark last node as leaf
        pCrawl.isEndOfWord = True

    def search(self, key):

        # Search key in the trie
        # Returns true if key presents
        # in trie, else false
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index]:
                return False
            pCrawl = pCrawl.children[index]

        return pCrawl != None and pCrawl.isEndOfWord

    # driver function


def main():
    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "anaswe", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

        # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))


if __name__ == '__main__':
    main()

# class Trie:
#     def __init__(self):
#         self.head = Node()
#
#     def __getitem__(self, key):
#         return self.head.children[key]
#
#     def __str__(self, depth=0):
#         return self.head.__str__()
#
#     def add(self, word):
#         current_node = self.head
#         word_finished = True
#
#         for i in range(len(word)):
#             if word[i] in current_node.children:
#                 current_node = current_node.children[word[i]]
#             else:
#                 word_finished = False
#                 break
#
#         if not word_finished:
#             while i < len(word):
#                 current_node.add_child(word[i])
#                 current_node.NodeCount += 1
#                 current_node = current_node.children[word[i]]
#                 i += 1
#
#         current_node.add_child(None)
#         current_node.NodeCount += 1
#         current_node = current_node.children[None]
#         current_node.data = word
#
#     def insert_word(self, word):
#         for word in word.split():
#             self.add(word)