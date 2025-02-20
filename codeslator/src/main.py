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
from utils.file_processor import read_input_file, process_output_code, get_file_extension, write_output_file
from utils.code_processor import get_system_message, get_user_prompt, translate_code_gpt, translate_code_claude
from utils.model_processor import get_model
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
    # Login to Anthropic & OpenAI
    anthropic_client = anthropic_login(api_key=anthropic_api_key)
    openai_client = openai_login(api_key=openai_api_key)

    # Read the code from file
    code_to_translate = read_input_file(filepath=code_filepath)

    # Set up system message and user prompt
    messages = [
        {"role": "system", "content": get_system_message(from_language=from_language, to_language=to_language)},
        {"role": "user", "content": get_user_prompt(code_to_translate=code_to_translate, from_language=from_language, to_language=to_language)}
    ]

    # TODO: Generate translated code 

    # TODO: Process output code

    # TODO: Write output code to file


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
    default_model_type = "gpt-4o"
    generative_model = get_model(str(args.model).lower()) if args.model else get_model(default_model_type.lower())
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