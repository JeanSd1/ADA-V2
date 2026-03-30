generate_cad_prototype_tool = {
    "name": "generate_cad_prototype",
    "description": "Generates a 3D wireframe prototype based on a user's description. Use this when the user asks to 'visualize', 'prototype', 'create a wireframe', or 'design' something in 3D.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "prompt": {
                "type": "STRING",
                "description": "The user's description of the object to prototype."
            }
        },
        "required": ["prompt"]
    }
}




write_file_tool = {
    "name": "write_file",
    "description": "Writes content to a file at the specified path. Overwrites if exists.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "path": {
                "type": "STRING",
                "description": "The path of the file to write to."
            },
            "content": {
                "type": "STRING",
                "description": "The content to write to the file."
            }
        },
        "required": ["path", "content"]
    }
}

read_directory_tool = {
    "name": "read_directory",
    "description": "Lists the contents of a directory.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "path": {
                "type": "STRING",
                "description": "The path of the directory to list."
            }
        },
        "required": ["path"]
    }
}

read_file_tool = {
    "name": "read_file",
    "description": "Reads the content of a file.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "path": {
                "type": "STRING",
                "description": "The path of the file to read."
            }
        },
        "required": ["path"]
    }
}

execute_command_tool = {
    "name": "execute_command",
    "description": "Executes a PowerShell command on Windows and returns the output. Use this to run any Windows command, script, or application.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "command": {
                "type": "STRING",
                "description": "The PowerShell command to execute. Examples: 'Get-Process', 'Start-Process notepad', 'dir C:\\', etc."
            }
        },
        "required": ["command"]
    }
}

open_application_tool = {
    "name": "open_application",
    "description": "Opens a Windows application or file. Can open exe files, documents, websites, etc.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "app_path": {
                "type": "STRING",
                "description": "The path or name of the application/file to open. Examples: 'notepad', 'C:\\Program Files\\...\\app.exe', 'https://google.com', 'document.txt', etc."
            },
            "arguments": {
                "type": "STRING",
                "description": "Optional: Command line arguments to pass to the application."
            }
        },
        "required": ["app_path"]
    }
}

delete_file_tool = {
    "name": "delete_file",
    "description": "Deletes a file from the system. Use with caution!",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "path": {
                "type": "STRING",
                "description": "The path of the file to delete."
            }
        },
        "required": ["path"]
    }
}

delete_directory_tool = {
    "name": "delete_directory",
    "description": "Deletes a directory and all its contents. Use with caution!",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "path": {
                "type": "STRING",
                "description": "The path of the directory to delete recursively."
            }
        },
        "required": ["path"]
    }
}

copy_file_tool = {
    "name": "copy_file",
    "description": "Copies a file from one location to another.",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "source": {
                "type": "STRING",
                "description": "Source file path."
            },
            "destination": {
                "type": "STRING",
                "description": "Destination file path."
            }
        },
        "required": ["source", "destination"]
    }
}

get_system_info_tool = {
    "name": "get_system_info",
    "description": "Gets system information about your computer (OS, processes, drives, etc).",
    "parameters": {
        "type": "OBJECT",
        "properties": {
            "info_type": {
                "type": "STRING",
                "description": "Type of info: 'processes', 'drives', 'environment', 'network', 'users', 'os'"
            }
        },
        "required": ["info_type"]
    }
}

tools_list = [{"function_declarations": [
    generate_cad_prototype_tool,
    write_file_tool,
    read_directory_tool,
    read_file_tool,
    execute_command_tool,
    open_application_tool,
    delete_file_tool,
    delete_directory_tool,
    copy_file_tool,
    get_system_info_tool
]}]


