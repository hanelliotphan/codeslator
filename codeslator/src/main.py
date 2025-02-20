# ---------------------------------------------------------------------------- #
# Author: Han-Elliot Phan                                                      #
# Email: hanelliotphan@gmail.com                                               #
#                                                                              #
# Last update: February 19, 2025                                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# main.py                                                                      #
#                                                                              #
# This file is for the main execution of the Codeslator project.               #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                               IMPORT LIBRARIES                               #
# ---------------------------------------------------------------------------- #

import argparse
import os

from utils.login import anthropic_login, openai_login
from utils.file_processor import process_output_code, get_file_extension, write_output_file
from models.gpt4 import gpt4_stream
from models.claude3 import claude3_stream


# ---------------------------------------------------------------------------- #
#                            MAIN STREAMLINE FUCNTION                          #
# ---------------------------------------------------------------------------- #

def main_streamline(
    anthropic_api_key,
    openai_api_key,
    code_filepath,
    from_language,
    to_language,
    generative_model_type,
    output_filepath
):
    """
    main_streamline -- Streamline the end-to-end process of the Codeslator 
    project
    """
    # TODO


def main():
    """
    main -- Main execution for the Codeslator project
    """
    # Get arguments from script command execution
    parser = argparse.ArgumentParser("Codeslator - Translate code from one programming language to another language")
    parser.add_argument("--file", "-f", required=True, help="[Required] Path to the code file to translate.")
    parser.add_argument("--from_language", "-fl", required=True, help="[Required] Language to translate the code from.")
    parser.add_argument("--to_language", "-tl", required=True, help="[Required] Language to translate the code to.")
    parser.add_argument("--model", "-m", required=False, help="[Optional] Model to translate the code. By default, GPT-4o model will be used.")
    args = parser.parse_args()

    # Initialize required variables
    anthropic_api_key_var = "ANTHROPIC_API_KEY"
    openai_api_key_var = "OPENAI_API_KEY"
    anthropic_api_key = os.environ.get(anthropic_api_key_var)
    openai_api_key = os.environ.get(openai_api_key_var)
    code_filepath = args.file
    from_language = args.from_language
    to_language = args.to_language
    gpt4_model = "gpt-4o"
    claude3_model = "claude-3-5-sonnet-20240620"
    generative_model = claude3_model if args.model else gpt4_model
    output_filepath = "./result_code" + get_file_extension(to_language.lower())

    # Codeslator streamline
    main_streamline(
        anthropic_api_key=anthropic_api_key,
        openai_api_key=openai_api_key,
        code_filepath=code_filepath,
        from_language=from_language,
        to_language=to_language,
        generative_model_type=generative_model,
        output_filepath=output_filepath
    )


# ---------------------------------------------------------------------------- #
#                                 MAIN EXECUTION                               #
# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    main()