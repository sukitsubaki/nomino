def restructure_name(file, params, index, folder_path):
    name, ext = os.path.splitext(file)
    return f"Reformatted_{name}{ext}"
