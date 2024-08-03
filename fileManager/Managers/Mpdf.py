import os
import re
from PyPDF2 import PdfReader, PdfWriter

from Managers.filemanager import FileManager


class PDFFileManager(FileManager):
    def __init__(self, path_file: str) -> None:
        super().__init__(path_file)
        self.reader = PdfReader(self.path_file)
        self.set_file_name()
        self.extension: str = '.pdf'

    def split_file(self) -> None:
        count = len(self.reader.pages)
        output_dir = f"{self.file_name}"
        os.makedirs(output_dir, exist_ok=True)
        
        for page_num in range(count):
            writer = PdfWriter()
            writer.add_page(self.reader.pages[page_num])
            
            output_pdf = f"{output_dir}/page_{page_num + 1}{self.extension}"
            with open(output_pdf, "wb") as output_file:
                writer.write(output_file)


    def merge_files(self, output_pdf: str) -> None:
        writer = PdfWriter()
        input_dir = f"{self.file_name}"
        page_files = [f"{input_dir}/{file}" for file in os.listdir(input_dir) if file.endswith('.pdf')]
        page_files.sort(key=lambda f: int(re.search(r'page_(\d+).pdf', f).group(1)))

        for file in page_files:
            reader = PdfReader(file)
            writer.add_page(reader.pages[0])
        
        with open(f'{output_pdf}_merged.{self.extension}', "wb") as output_file:
            writer.write(output_file)
        
