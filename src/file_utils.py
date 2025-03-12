import os
from rename_strategies.strategy_handler import apply_rename_strategy

def get_files(folder_path, extension_filter=None):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    if extension_filter:
        return [f for f in files if f.endswith(extension_filter)]
    return files

def rename_files(files, choice, params, folder_path):
    new_names = []
    for index, file in enumerate(files, start=1):
        new_name = apply_rename_strategy(file, choice, params, index, folder_path)
        os.rename(os.path.join(folder_path, file), os.path.join(folder_path, new_name))
        new_names.append(new_name)
    return new_names
