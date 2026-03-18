import os

def get_files_info(working_directory, directory="."):
    joined = os.path.join(working_directory, directory)
    abs_work = os.path.abspath(working_directory)
    abs_target = os.path.abspath(joined)

    work_with_sep = abs_work if abs_work.endswith(os.sep) else abs_work + os.sep
    inside = abs_target == abs_work or abs_target.startswith(work_with_sep)
    if not inside:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(abs_target): 
        return f'Error: "{directory}" is not a directory'
    
    try:
        entries = os.listdir(abs_target)
        lines = []
        
        for name in entries:
            full = os.path.join(abs_target, name)
            is_dir = os.path.isdir(full)
            size = os.path.getsize(full) if os.path.isfile(full) else os.path.getsize(full)
            lines.append(f"- {name}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(lines)
    except Exception as e:
        return f"Error: {e}"