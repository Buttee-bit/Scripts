from pydantic import BaseModel


class InputFile(BaseModel):
    path: str
    file_extension: str

    @classmethod
    def from_path(cls, path: str):
        file_extension = path.split('.')[-1].lower()
        return cls(path=path, file_extension=file_extension)
