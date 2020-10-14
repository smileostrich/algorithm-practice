class Trie:
    def __init__(self):
        self.head = Node()

    def __getitem__(self, key):
        return self.head.children[key]

    def __str__(self, depth=0):
        return self.head.__str__()

    def add(self, word):
        current_node = self.head
        word_finished = True

        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_finished = False
                break

        if not word_finished:
            while i < len(word):
                current_node.add_child(word[i])
                current_node.NodeCount += 1
                current_node = current_node.children[word[i]]
                i += 1

        current_node.add_child(None)
        current_node.NodeCount += 1
        current_node = current_node.children[None]
        current_node.data = word

    def insert_word(self, word):
        for word in word.split():
            self.add(word)