import os

MAX_CHARS = 10000


def get_files_info(working_directory, directory="."):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, directory))

    if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_file_path):
        return f'Error: "{directory}" is not a directory'

    try:
        entries_info = []
        with os.scandir(abs_file_path) as entries:
            for entry in entries:
                stat_result = entry.stat()
                entries_info.append(
                    f"- {entry.name}: file_size={stat_result.st_size} bytes, is_dir={entry.is_dir()}"
                )
        return "\n".join(entries_info)
    except Exception as e:
        return f"Error listing files: {e}"

def get_file_content(working_directory, file_path):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: "{file_path}" is not a file'

    try:
        contents = ""
        with open(abs_file_path, "r") as f:
            contents = f.read(MAX_CHARS + 1)
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
            return contents
    except Exception as e:
        return f"Error reading file: {e}"

def write_file(working_directory, file_path, content):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if os.path.commonpath([abs_working_dir, abs_file_path]) != abs_working_dir:
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    head, _ = os.path.split(abs_file_path)
    if not os.path.exists(head):
        os.makedirs(head)

    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
    except Exception as e:
        return f'Error writing file "{file_path}": {e}'
    
    return f'Successfully wrote to "{abs_file_path}" ({len(content)} characters written)'

def get_file_content_alt(working_directory, file_path):

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try:
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'

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
