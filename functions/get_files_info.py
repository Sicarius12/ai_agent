
import os

def get_files_info(working_directory, directory="."):

    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    if os.path.commonpath([abs_working_dir, full_path]) != abs_working_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    try:
        entries_info = []
        with os.scandir(full_path) as entries:
            for entry in entries:
                stat_result = entry.stat()
                entries_info.append(
                    f"- {entry.name}: file_size={stat_result.st_size} bytes, is_dir={entry.is_dir()}"
                )
        return "\n".join(entries_info)
    except Exception as e:
        return f"Error listing files: {e}"
    
def get_file_content(working_directory, filepath):

    abs_working_dir = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, filepath))

    if os.path.commonpath([abs_working_dir, full_path]) != abs_working_dir:
        return f'Error: Cannot list "{filepath}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_path):
        return f'Error: "{filepath}" is not a file'
    
    MAX_CHARS = 10000
    try:
        contents = ""
        with open(full_path, "r") as f:
            contents = f.read(MAX_CHARS + 1)
            if len(contents) > MAX_CHARS:
                contents = contents[:MAX_CHARS] + f'\n[...File "{filepath}" truncated at 10000 characters]'
            return contents
    except Exception as e:
        return f"Error reading file: {e}"

def get_files_info_alt(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
