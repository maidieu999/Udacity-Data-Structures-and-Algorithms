import sys
import collections

class Node:
    def __init__(self, char=None, left=None, right=None):
        self.char = char
        self.left = left
        self.right = right

def huffman_code_tree(node, binString=''):
    if node.char is not None:
        return {node.char: binString}
    # Recursively traverse the tree to get the huffman code for each character
    return {**huffman_code_tree(node.left, binString + '0'), **huffman_code_tree(node.right, binString + '1')}

def build_huffman_tree(text):
    freq = collections.Counter(text)

    # If there is only one character in the text, return a tree with a single node
    if len(freq) == 1:
        char = next(iter(freq))
        return Node(char), {char: '0'}
    
    # Build the huffman tree
    nodes = [Node(char=char) for char in freq]
    while len(nodes) > 1:
        nodes.sort(key=lambda x: freq[x.char])
        left = nodes.pop(0)
        right = nodes.pop(0)
        new_node = Node(left=left, right=right)
        nodes.append(new_node)
        freq[new_node.char] = freq[left.char] + freq[right.char]

    root = nodes[0]
    huffman_dict = huffman_code_tree(root)
    return root, huffman_dict

def huffman_encoding(text):
    if len(text) == 0:
        return '', {}

    root, huffman_dict = build_huffman_tree(text)
    huffman_codes = [huffman_dict[char] for char in text]
    huffman_code = ''.join(huffman_codes)
    return huffman_code, huffman_dict

def huffman_decoding(huffman_code, huffman_dict):
    # Check for empty input strings or invalid inputs
    if not huffman_code or not huffman_dict:
        print("Error: Invalid input")
        return ""

    reversed_dict = {v: k for k, v in huffman_dict.items()}

    result = ''
    current_pos = 0
    while current_pos < len(huffman_code):
        found_match = False
        for code in reversed_dict:
            if huffman_code.startswith(code, current_pos):
                result += reversed_dict[code]
                current_pos += len(code)
                found_match = True
                break
        if not found_match:
            print("Error: Huffman code not found in the dictionary")
            return ""
    return result

def test(data):
    if type(data) != str:
        data = str(data)
        
    if len(data) == 0:
        print("Data is empty. No need to encode or decode.")
        return

    print(f"Data: {data}")
    data_size = sys.getsizeof(data)
    print(f"Data Size: {data_size}")

    encoded_data, huffman_dict = huffman_encoding(data)
    encoded_data_size = sys.getsizeof(int(encoded_data, base=2))

    print(f"Encoded Data: {encoded_data}")
    print(f"Encoded Data Size: {encoded_data_size}")
    print(f'Size Reduced: {data_size - encoded_data_size}')

    decoded_data = huffman_decoding(encoded_data, huffman_dict)
    decoded_data_size = sys.getsizeof(decoded_data)

    print(f"Decoded Data: {decoded_data}")
    print(f"Decoded Data Size: {decoded_data_size}\n")


if __name__ == "__main__":
    test("12345")
    test("ABCDE")
    test("This is probelem 3 of project 2.")
    test("AAAAAAA")
    test("")
    test(101010101)
