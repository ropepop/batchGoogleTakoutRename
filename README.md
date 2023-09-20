README

This Python script renames files in a directory based on their duplicate numbers. The script first finds all files in the directory with the .json extension. It then splits each file name into the following parts:

Bare file name: The part of the file name before the duplicate number and file extension.
Duplicate number: The part of the file name between the opening and closing parentheses.
File extension: The part of the file name after the dot.
The script then constructs a new file name for each file using the following format:

Bare file name (Duplicate number).File extension.json
The script then renames each file using its new file name.

Example

The following example shows how the script would rename a file:

Old file name: file_name_1(1).json
New file name: file_name(1).json
Usage

To use the script, simply run it from the command line and specify the path to the directory containing the files that you want to rename. For example, to rename all files in the current directory, you would run the following command:

python rename_files.py
Note

The script will overwrite existing files with the same name. Be sure to back up your files before running the script.
