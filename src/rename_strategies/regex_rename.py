import re

def rename_with_regex(file, params, index, folder_path):
    name, ext = os.path.splitext(file)
    pattern, replacement = params.split(',')
    return re.sub(pattern, replacement, name) + ext
