# ---------------------------------------------------------------------------- #
# Author: Han-Elliot Phan                                                      #
# Email: hanelliotphan@gmail.com                                               #
#                                                                              #
# Last update: February 19, 2025                                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# file_processor.py                                                            #
#                                                                              #
# This file is for processing input/outfile files:                             #
# 1. TBA
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                               IMPORT LIBRARIES                               #
# ---------------------------------------------------------------------------- #

import logging
import sys


# ---------------------------------------------------------------------------- #
#                          FILE PROCESSING FUNCTIONS                           #
# ---------------------------------------------------------------------------- #

def read_input_file(filepath):
    """
    read_input_file -- Read content of file
    """


def process_output_code(code_string):
    """
    process_output_code -- Process the output code to ensure it is executable
    """
    code_lines = code_string.split("\n")
    for i in range(len(code_lines)):
        if "```" in code_lines[i]:
            code_lines[i] = ""
    return "\n".join(code_lines)


def get_file_extension(code_language):
    """
    get_file_extension -- Get file extension based on the chosen code language
    """
    extensions = {
        "c": ".c",
        "c++": ".cpp",
        "c#": ".cs",
        "dart": ".dart",
        "elixir": ".ex",
        "erlang": ".erl",
        "go": ".go",
        "golang": ".go",
        "java": ".java",
        "javascript": ".js",
        "kotlin": ".kt",
        "php": ".php",
        "python2": ".py",
        "python3": ".py",
        "racket": ".rkt",
        "ruby": ".rb",
        "rust": ".rs",
        "scala": ".scala",
        "swift": ".swift",
        "typescript": ".ts"
    }
    if code_language not in extensions:
        logging.error(msg="[file_processor.py] get_file_extension: The coding language you have chosen is not currently supported. Please choose from the following options:")
        for language in extensions.keys():
            logging.info(msg=f"- {language.capitalize()}")
        sys.exit(1)
    return extensions[code_language]


def write_output_file(filepath, output):
    """
    generate_output_file -- Write output to file
    """
    with open(filepath, "w") as f:
        f.write(output)