import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from Huffman import *
import mammoth


class HuffmanCodeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Huffman Coding")
        self.root.geometry("600x400")
        self.root.configure(bg="light blue")

        self.file_frame = tk.Frame(root, bg="white", padx=10, pady=10)
        self.file_frame.pack(fill="x", padx=10, pady=5)

        self.file_label = tk.Label(
            self.file_frame, text="Selected File: None", bg="white", fg="black", font=("Arial", 12, "bold")
        )
        self.file_label.pack(side="left", fill="x", expand=True)

        self.choose_file_button = tk.Button(
            self.file_frame, text="Choose File", command=self.choose_file, bg="light blue", fg="black", font=("Arial", 12, "bold")
        )
        self.choose_file_button.pack(side="right")

        self.stats_frame = tk.Frame(root, bg="light blue", padx=10, pady=10)
        self.stats_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.grid_title = tk.Label(
            self.stats_frame,
            text="Huffman Coding",
            bg="light blue",
            fg="black",
            font=("Arial", 16, "bold"),
            anchor="center"
        )
        self.grid_title.pack(pady=(30, 10))

        self.grid_frame = tk.Frame(self.stats_frame, bg="light blue")
        self.grid_frame.place(relx=0.5, rely=0.5, anchor="center")

        self.stats_labels = [
            "Docx file Total Characters",
            "Number of Unique Characters",
            "Entropy (bits/char)",
            "Huffman Average Bits/Character",
            "NASCII",
            "Nhuffman",
            "Compression Percentage"
        ]

        self.stats_entries = {}
        for i, label in enumerate(self.stats_labels):
            tk.Label(
                self.grid_frame,
                text=label,
                bg="light blue",
                fg="black",
                font=("Arial", 12, "bold"),
                anchor="w"
            ).grid(row=i, column=0, padx=10, pady=5, sticky="w")

            entry = tk.Entry(
                self.grid_frame,
                font=("Arial", 12),
                state="readonly",
                justify="center",
                width=30
            )
            entry.grid(row=i, column=1, padx=10, pady=5, sticky="w")
            self.stats_entries[label] = entry

        self.table_button = tk.Button(
            root, text="Show Table (Symbols Freq, Prob...)", command=self.show_huffman_table, bg="white", fg="black", font=("Arial", 12, "bold")
        )
        self.table_button.pack(pady=10)

        self.footer_frame = tk.Frame(root, bg="light blue")
        self.footer_frame.pack(fill="x", side="bottom", padx=10, pady=5)

        self.footer_label = tk.Label(
            self.footer_frame,
            text="Developed by: Jubran Khoury and Mohammad Abdelkareem",
            bg="light blue",
            fg="black",
            font=("Arial", 10, "bold"),
        )
        self.footer_label.pack(side="top", pady=5)

        self.huffman = None 

    def choose_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Word Documents", "*.docx")],
            title="Choose a Word Document"
        )
        if file_path:
            self.file_label.config(text=f"Selected File: {file_path}")
            self.process_file(file_path)
        else:
            messagebox.showwarning("File Selection Error", "No file selected!")

    def process_file(self, file_path):
        try:
            with open(file_path, "rb") as file:
                result = mammoth.extract_raw_text(file)
                text = result.value.strip()
                if not text:
                    raise ValueError("The selected file is empty or contains unsupported content.")
                self.huffman = HuffmanCoding(text, modify_text=True)
                self.update_stats()
        except Exception as e:
            messagebox.showerror("Processing Error", f"Error processing file: {str(e)}")

    def update_stats(self):
        if not self.huffman:
            return

        stats_data = {
            "Docx file Total Characters": len(self.huffman.text),
            "Number of Unique Characters": len(set(self.huffman.text)),
            "Entropy (bits/char)": f"{self.huffman.entropy:.4f}",
            "Huffman Average Bits/Character": f"{self.huffman.average_bits_per_character():.4f}",
            "NASCII": self.huffman.total_bits_ascii(),
            "Nhuffman": self.huffman.total_bits_huffman(),
            "Compression Percentage": f"{self.huffman.compression_percentage():.2f}%",
        }

        for label, value in stats_data.items():
            self.stats_entries[label].config(state="normal")
            self.stats_entries[label].delete(0, tk.END)
            self.stats_entries[label].insert(0, value)
            self.stats_entries[label].config(state="readonly")

    def show_huffman_table(self):
        if not self.huffman:
            messagebox.showwarning("No Data", "Please process a file first.")
            return

        table_window = tk.Toplevel(self.root)
        table_window.title("Huffman Encoding Table")
        table_window.geometry("600x400")
        table_window.configure(bg="light blue")

        columns = ["Symbol", "Frequency", "Probability", "Codeword", "Length"]
        table = ttk.Treeview(table_window, columns=columns, show="headings")

        for col in columns:
            table.heading(col, text=col, anchor="center")
            table.column(col, anchor="center", width=100)

        for row in self.huffman.results_table():
            table.insert("", "end", values=row)

        table.pack(fill="both", expand=True, padx=10, pady=10)

        scrollbar = ttk.Scrollbar(table_window, orient="vertical", command=table.yview)
        table.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")


if __name__ == "__main__":
    root = tk.Tk()
    gui = HuffmanCodeGUI(root)
    root.mainloop()
