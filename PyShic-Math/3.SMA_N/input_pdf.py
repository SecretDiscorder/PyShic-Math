import PyPDF2
import sys, os
from ast import keyword
from fpdf import FPDF
hruf_latin = {
    "a": "._", "b": "_...", "c": "_._.", "d": "_..", "e": ".", "f": ".._.", "g": "__.", "h": "....", "i": "..",
    "j": ".___", "k": "_._", "l": "._..", "m": "__", "n": "_.", "o": "___", "p": ".__.", "q": "__._", "r": "._.",
    "s": "...", "t": "_", "u": "..._", "w": ".__", "x": "_.._", "y": "_.__", "z": "__..", "1": ".._", "v": ".____",
    "2": "..___", "3": "...__", "4": "...._", "5": ".....", "6": "_....", "7": "__...", "8": "___..", "9": "____.",
    "0": "_____"
}

def reverse_morse_translate(morse_code):
    reverse_dict = {value: key for key, value in hruf_latin.items()}
    morse_chars = morse_code.strip().split(" ")
    text = "".join([reverse_dict[char] if char in reverse_dict else " " for char in morse_chars])
    return text

def morse_translate(text):
    morse_code = []
    for char in text.lower():
        if char in hruf_latin:
            morse_code.append(hruf_latin[char])
        else:
            morse_code.append(" ")  # Menggunakan spasi jika karakter tidak ada dalam dictionary
    return " ".join(morse_code)

def read_pdf(file_path):
    pdf_text = ""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            pdf_page = pdf_reader.pages[page_num]
            pdf_text += pdf_page.extract_text()
    return pdf_text
    
def write_pdf(file_path, text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=text, ln=1)

    pdf.output(file_path)

input_file_path = "input.pdf"

# Membaca isi file PDF
input_text = read_pdf(input_file_path)

# Konversi teks menjadi kode Morse
morse_result = morse_translate(input_text)

# Menyimpan hasil ke dalam file output.pdf
write_pdf("output.pdf", morse_result)

# Mendekripsi hasil kembali menjadi teks
text_result = reverse_morse_translate(morse_result)

# Menyimpan hasil dekripsi ke dalam file outputtext.pdf
write_pdf("outputtext.pdf", text_result)
#
