class RouteTrieNode:
    # A node in the RouteTrie
    def __init__(self):
        self.children = {}
        self.handler = None  # Handler for the end of path

class RouteTrie:
    # Stores routes and their associated handlers
    def __init__(self, handler=""):
        self.root = RouteTrieNode()
        self.root.handler = handler

    def insert(self, path, handler):
        # Inserts a path and its handler into the trie.
        node = self.root
        parts = self._split_path(path)

        for part in parts:
            if part not in node.children:
                node.children[part] = RouteTrieNode()
            node = node.children[part]
        
        node.handler = handler

    def find(self, path):
        # Finds the handler for a given path.
        node = self.root
        parts = self._split_path(path)

        for part in parts:
            if part not in node.children:
                return None
            node = node.children[part] 

        return node.handler
    
    def _split_path(self, path):
        # Splits a path into parts
        if path == "/":
            return []
        return path.strip("/").split("/")

class Router:
    # Routes requests to handlers.
    def __init__(self, root_handler, not_found_handler=None):
        self.trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Adds a handler for a given path.
        self.trie.insert(path, handler)

    def lookup(self, path):
        # Looks up the handler for a given path.
        if not path:
            return self.trie.root.handler

        handler = self.trie.find(path)
        if handler is not None:
            return handler
        else:
            return self.not_found_handler

# Test Case
router = Router("root handler", "not found handler")
router.add_handler("/blog", "blog handler")
router.add_handler("/blog/article1", "article1 handler")

print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/blog"))  # should print 'blog handler'
print(router.lookup("/blog/article1"))  # should print 'article1 handler'
print(router.lookup("/blog/article2"))  # should print 'not found handler'
print(router.lookup("")) # should print root handler
