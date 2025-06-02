import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger, PdfReader, PdfWriter

class PDFTool:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Merger & Splitter")
        self.root.geometry("400x300")

        tk.Button(root, text="Merge PDFs", width=25, command=self.merge_pdfs).pack(pady=20)
        tk.Button(root, text="Split PDF", width=25, command=self.split_pdf).pack(pady=20)

    def merge_pdfs(self):
        files = filedialog.askopenfilenames(title="Select PDFs to Merge", filetypes=[("PDF Files", "*.pdf")])
        if not files:
            return

        merger = PdfMerger()
        for pdf in files:
            merger.append(pdf)

        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if save_path:
            merger.write(save_path)
            merger.close()
            messagebox.showinfo("Success", f"PDFs merged and saved to:\n{save_path}")

    def split_pdf(self):
        file = filedialog.askopenfilename(title="Select PDF to Split", filetypes=[("PDF Files", "*.pdf")])
        if not file:
            return

        pdf = PdfReader(file)
        num_pages = len(pdf.pages)

        output_dir = filedialog.askdirectory(title="Select Folder to Save Split PDFs")
        if not output_dir:
            return

        for i in range(num_pages):
            writer = PdfWriter()
            writer.add_page(pdf.pages[i])
            output_path = os.path.join(output_dir, f"page_{i+1}.pdf")
            with open(output_path, "wb") as f:
                writer.write(f)

        messagebox.showinfo("Success", f"Split into {num_pages} files at:\n{output_dir}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PDFTool(root)
    root.mainloop()
