from Managers.filemanager import FileManager
from Managers.Mpdf import PDFFileManager
from Managers.MWord import WordFileManager
from Managers.MExel import ExcelFileManager

from schemas import InputFile


class FileManagerFactory:
    @staticmethod
    def get_file_manager(input_file: InputFile) -> FileManager:
        if input_file.file_extension == 'pdf':
            return PDFFileManager(input_file)
        elif input_file.file_extension == 'docx':
            return WordFileManager(input_file)
        elif input_file.file_extension == 'xlsx':
            return ExcelFileManager(input_file)
        else:
            raise ValueError(f"Unsupported file extension: {input_file.file_extension}")
