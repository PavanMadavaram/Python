#Day 44 - Context Managers  
class FileManager:
    def __enter__(self):
        self.file = open("data.txt", "w")
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

with FileManager() as f:
    f.write("Day 44 data")
print("File managed safely")
