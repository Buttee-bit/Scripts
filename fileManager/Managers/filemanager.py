from schemas import InputFile


class FileManager:
    def __init__(self, file:InputFile) -> None:
        self.path_file: str = file.path
        self.file_name: str = self.set_file_name()
        self.extension: str = file.file_extension
        self.reader = None

    def set_file_name(self) -> str:
        self.file_name = self.path_file.split('/')[-1].split('.')[0]


    def get_file_name(self) -> str:
        return self.file_name
    
    def split_file(self):
        ...
    
    def merge_files(self):
        ...