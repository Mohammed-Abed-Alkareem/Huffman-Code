import heapq
from collections import Counter, defaultdict
from math import log2
from docx import Document
import mammoth

class HuffmanCoding:
    def __init__(self, text):
        self.text = text.lower().replace("\n", "")  # Normalize the text
        self.frequencies = self.calculate_frequencies()
        self.probabilities = self.calculate_probabilities()
        self.entropy = self.calculate_entropy()
        self.codes = self.generate_huffman_codes()

    def calculate_frequencies(self):
        return Counter(self.text)

    def calculate_probabilities(self):
        total_characters = sum(self.frequencies.values())
        return {char: freq / total_characters for char, freq in self.frequencies.items()}

    def calculate_entropy(self):
        return -sum(p * log2(p) for p in self.probabilities.values() if p > 0)

    def generate_huffman_codes(self):
        heap = [[weight, [symbol, ""]] for symbol, weight in self.probabilities.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            lo = heapq.heappop(heap)
            hi = heapq.heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

        return dict(sorted(heapq.heappop(heap)[1:], key=lambda x: (len(x[1]), x[0])))

    def average_bits_per_character(self):
        return sum(len(self.codes[char]) * self.probabilities[char] for char in self.codes)

    def total_bits_huffman(self):
        return sum(len(self.codes[char]) * self.frequencies[char] for char in self.codes)

    def total_bits_ascii(self):
        return len(self.text) * 8

    def compression_percentage(self):
        n_ascii = self.total_bits_ascii()
        n_huffman = self.total_bits_huffman()
        return (1 - n_huffman / n_ascii) * 100

    def results_table(self):
        table = [
            [char, self.probabilities[char], self.codes[char], len(self.codes[char])]
            for char in sorted(self.codes.keys())
        ]
        return table