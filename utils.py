import os

def read_file(file) -> str:
    content = file.read()
    return content.decode("utf-8") if isinstance(content, bytes) else content

def chunk_code(code: str, max_lines: int = 50) -> list:
    lines = code.splitlines()
    return ["\n".join(lines[i:i+max_lines]) for i in range(0, len(lines), max_lines)]

