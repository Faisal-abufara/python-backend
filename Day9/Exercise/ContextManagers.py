file_path = "FaisalFile.txt"
class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
        return False


with FileManager(file_path, "w") as file:
    file.write("Hello from custom context manager!\nDid know why did it work but here it;s")

with FileManager(file_path, "r") as file:
    content = file.read()
    print(content)