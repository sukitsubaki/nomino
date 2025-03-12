def add_text(file, params, index, folder_path):
    name, ext = os.path.splitext(file)
    return f"{params}{name}{ext}"
