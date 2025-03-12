def log_changes(old_files, new_files):
    with open("rename_log.txt", "w") as log:
        for old, new in zip(old_files, new_files):
            log.write(f"{old} -> {new}\n")

def undo_last_rename():
    try:
        with open("rename_log.txt", "r") as log:
            lines = log.readlines()
        for line in reversed(lines):
            old, new = line.strip().split(" -> ")
            os.rename(new, old)
        print("Undo successful!")
    except Exception as e:
        print(f"Error during undo: {e}")
