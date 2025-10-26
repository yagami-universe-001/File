import os

class FileHandler:
    def get_file_size(self, file_path):
        return os.path.getsize(file_path)
    def format_file_size(self, size_bytes):
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024
    # ...more file helpers...
