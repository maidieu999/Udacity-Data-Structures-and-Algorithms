import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash=None):
        self._timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self._calc_hash()

    @property
    def timestamp(self):
        return self._timestamp

    def _calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{self.timestamp}-{self.data}-{self.previous_hash}".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def __str__(self):
        return (f'Time: {self.timestamp}, Data: {self.data}, SHA256 Hash: {self.hash}, Previous Hash: {self.previous_hash}')

class BlockNode:
    def __init__(self, block):
        self.block = block
        self.next = None

class BlockChain:
    def __init__(self):
        self._head = None
        self._tail = None
        self._previous_hash = "0" * 64

    def append(self, data):
        new_block = Block(datetime.now(), data, self._previous_hash)
        new_node = BlockNode(new_block)

        if self._head is None:
            self._head = new_node
            self._tail = self._head
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._previous_hash = new_block.hash

    @staticmethod
    def _format_time(timestamp):
        return timestamp.strftime("%Y-%m-%d %H:%M:%S")
    
    def __str__(self):
        blockchain_str = ""
        current_block = self._head
        block_index = 0
        while current_block:
            block = current_block.block
            blockchain_str += (f'Block: {block_index}, Data: {block.data}, Time: {self._format_time(block.timestamp)}, '
                            f'\nSHA256 Hash: {block.hash}, \nPrevious Hash: {block.previous_hash}\n')
            block_index += 1
            current_block = current_block.next
        return blockchain_str

# test cases
blockchain = BlockChain()
blockchain.append("A")
blockchain.append("B")
blockchain.append("C")
blockchain.append("D")

print("Test Case 1 - should print 4 blocks A, B, C, D")
print(blockchain)
