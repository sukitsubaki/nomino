def number_files(file, params, index, folder_path):
    name, ext = os.path.splitext(file)
    return f"{params}_{str(index).zfill(4)}{ext}"
