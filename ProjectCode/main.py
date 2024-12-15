from Huffman import *
import mammoth
from prettytable import PrettyTable

if __name__ == "__main__":
    # Replace with the path to your .docx file
    docx_file = "Huffman-Code\ProjectCode\To+Build+A+Fire+by+Jack+London.docx"
    with open(docx_file, "rb") as file:
        result = mammoth.extract_raw_text(file)
        text = result.value
    # print(text)
    # print(type(text))

    print("Number of characters in the text: ", len(text))
    

    unique_uppercase_characters = len(set(filter(str.isupper, text)))
    print(f"Number of unique uppercase characters in the text: {unique_uppercase_characters}")
    
    number_of_unique_characters = len(set(text))
    print(f"Number of unique characters in the text: {number_of_unique_characters}")


    print("\nHuffman Coding Results:")


    huffman = HuffmanCoding(text, modify_text=True)

    print(f"Number of characters in the text after normalization: {len(huffman.text)}")
    print(f"Number of unique characters in the text after normalization: {len(set(huffman.text))}")
    print(len(huffman.text) == sum(huffman.frequencies.values()))
    print(f"Number of characters in the text after normalization: {sum(huffman.frequencies.values())}")

    print(f"Entropy: {huffman.entropy:.4f} bits/character")
    print(f"Average Bits per Character: {huffman.average_bits_per_character():.4f}")
    print(f"Total Bits (ASCII): {huffman.total_bits_ascii()}")
    print(f"Total Bits (Huffman): {huffman.total_bits_huffman()}")
    print(f"Compression Percentage: {huffman.compression_percentage():.2f}%")





    print("\nResults Table:")
    results_table = PrettyTable()
    results_table.field_names = ["Symbol", "Frequrncy", "Probability", "Codeword", "Length"]
    for row in huffman.results_table():
        results_table.add_row(row)
    print(results_table)




### Without modifying the text
    huffman = HuffmanCoding(text, modify_text=False)

    print(f"Number of characters in the text after normalization: {len(huffman.text)}")
    print(f"Number of unique characters in the text after normalization: {len(set(huffman.text))}")
    print(len(huffman.text) == sum(huffman.frequencies.values()))
    print(f"Number of characters in the text after normalization: {sum(huffman.frequencies.values())}")

    print(f"Entropy: {huffman.entropy:.4f} bits/character")
    print(f"Average Bits per Character: {huffman.average_bits_per_character():.4f}")
    print(f"Total Bits (ASCII): {huffman.total_bits_ascii()}")
    print(f"Total Bits (Huffman): {huffman.total_bits_huffman()}")
    print(f"Compression Percentage: {huffman.compression_percentage():.2f}%")


    print("\nResults Table:")
    results_table = PrettyTable()
    results_table.field_names = ["Symbol", "Frequrncy", "Probability", "Codeword", "Length"]
    for row in huffman.results_table():
        results_table.add_row(row)
    print(results_table)
