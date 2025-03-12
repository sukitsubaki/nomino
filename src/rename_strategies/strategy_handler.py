import os
import re
from rename_strategies.numbering import number_files
from rename_strategies.text_removal import remove_text
from rename_strategies.text_addition import add_text
from rename_strategies.restructuring import restructure_name
from rename_strategies.exif_rename import rename_by_exif
from rename_strategies.regex_rename import rename_with_regex
from rename_strategies.sorting import sort_by_date

def apply_rename_strategy(file, choice, params, index, folder_path):
    strategies = {
        '1': number_files,
        '2': remove_text,
        '3': add_text,
        '4': restructure_name,
        '5': rename_by_exif,
        '9': rename_with_regex,
        '10': sort_by_date
    }
    return strategies.get(choice, lambda f, p, i, fp: f)(file, params, index, folder_path)
