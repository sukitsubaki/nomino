def remove_text(file, params, index, folder_path):
    name, ext = os.path.splitext(file)
    return name.replace(params, "") + ext
