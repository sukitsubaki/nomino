# Nomino - Smart File Renamer

Nomino is a versatile file renaming tool designed to simplify the management of large numbers of files. With support for various renaming strategies, it can automatically number files, add or remove text, restructure filenames, rename based on EXIF data and much more.

## Features

**Multiple Renaming Strategies**:
- Number files sequentially.
- Remove text from filenames.
- Add custom text to filenames.
- Restructure filenames with a predefined format.
- Rename files based on EXIF data (e.g. photos).
- Use regex patterns to rename files.
- Sort files into subfolders by date.
  
**Preview and Undo**:
- Preview file renaming before applying changes.
- Undo the last rename operation.

**Flexible File Filtering**:
- Filter files by extensions before renaming.
  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/nomino.git
   cd nomino
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python src/main.py
   ```
2. Enter the folder path where your files are located.
3. Choose a renaming strategy from the menu:
   - ```1``` Number all files sequentially.
   - ```2``` Remove text from filenames.
   - ```3``` Add text to filenames.
   - ```4``` Restructure filenames.
   - ```5``` Rename files based on EXIF data (photos).
   - ```6``` Filter files by extension.
   - ```7``` Preview rename before applying.
   - ```8``` Undo last rename.
   - ```9``` Rename using regex pattern.
   - ```10``` Sort files into subfolders by date.
4. Provide additional parameters (if required) for the chosen option (e.g. text to remove, text to add, regex pattern).
5. Nomino will rename your files accordingly and log the changes in a rename_log.txt file.

## Requirements
- Python 3.x
- Pillow (for EXIF handling)

## File Structure
```src/main.py``` Main entry point of the program.

```src/cli.py``` Contains the menu for user interactions.

```src/file_utils.py``` Handles file operations such as renaming and filtering.

```src/log_utils.py``` Logs the renaming process and supports undo.

```src/progress.py``` Displays a progress bar during renaming operations.

```src/exif_utils.py``` Extracts EXIF data from images.

```src/rename_strategies/``` Contains all the renaming strategies.

## Contributing
Feel free to fork the repository, submit issues, or create pull requests if you'd like to contribute. This README provides a comprehensive guide to install, use and understand the functionality of Nomino. Let me know if you'd like to make any adjustments!
