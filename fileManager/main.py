from Factory import FileManagerFactory
from schemas import InputFile





if __name__ == "__main__":
    input_path = r"PATH/FILE.EXTENSION"

    input_file = InputFile.from_path(input_path)
    file_manager = FileManagerFactory.get_file_manager(input_file)
    #Decomposite
    file_manager.split_file()
    #Merge
    file_manager.merge_files(output_pdf=f"{file_manager.get_file_name()}")