import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from Huffman import *
from prettytable import PrettyTable
import mammoth

class HuffmanCodeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Huffman Code GUI")

       

        self.file_button = tk.Button(root, text="Choose File", command=self.choose_file)
        self.file_button.pack()

        self.result_label = tk.Label(root, text="Encoded text will appear here")
        self.result_label.pack()

    
    def choose_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "rb") as file:
                result = mammoth.extract_raw_text(file)
                text = result.value

            encoded_text = self.huffman_encode(text)
            self.result_label.config(text=f"Encoded Text Results: \n {encoded_text}")
        else:
            messagebox.showwarning("Input Error", "Please select a file to encode")


            


    def huffman_encode(self, text):
        huffman = HuffmanCoding(text, modify_text=True)

        results_table = PrettyTable()
        results_table.field_names = ["Symbol", "Frequency", "Probability", "Codeword", "Length"]
        for row in huffman.results_table():
            results_table.add_row(row)

        #convert to str to display in the GUI
        return str(results_table)
        
       

if __name__ == "__main__":
    root = tk.Tk()
    gui = HuffmanCodeGUI(root)
    root.mainloop()
   