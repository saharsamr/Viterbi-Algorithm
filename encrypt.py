import Node
import heapq


def generate_codes(current_node, current_code, codes):
    if current_node is None:
        return
    if current_node.val != "*":
        codes[current_node.val] = current_code
    right_code = current_code + '1'
    generate_codes(current_node.right, right_code, codes)
    left_code = current_code + '0'
    generate_codes(current_node.left, left_code, codes)


def encrypt(probs, string, codes):
    min_heap = []
    for prob in xrange(0, len(probs)):
        min_heap.append(Node.Node(chr(ord('a')+prob), probs[prob]))
    heapq.heapify(min_heap)

    for i in xrange(0, 25):
        min1 = heapq.heappop(min_heap)
        min2 = heapq.heappop(min_heap)
        new_freq = min1.freq + min2.freq
        new_node = Node.Node('*', new_freq)
        new_node.left = min1
        new_node.right = min2
        heapq.heappush(min_heap, new_node)

    generate_codes(min_heap[0], '', codes)

    encoded = ''
    for s in string:
        encoded += codes[s]

    return encoded

