import zipfile

def decompress_zip(zip_file_path, destination_folder):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(destination_folder)

# Example usage
zip_file_path = r'D:\Master\Programación para la ciencia de datos\PEC4\twitter_reduced.zip'
destination_folder = r'D:\Master\Programación para la ciencia de datos\PEC4'
decompress_zip(zip_file_path, destination_folder)