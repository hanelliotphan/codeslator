# ---------------------------------------------------------------------------- #
# Author: Han-Elliot Phan                                                      #
# Email: hanelliotphan@gmail.com                                               #
#                                                                              #
# Last update: February 20, 2025                                               #
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

from utils.file_processor import read_input_file, process_output_code, get_file_extension, write_output_file
from utils.code_processor import get_system_message, get_user_prompt
from utils.model_processor import get_model_translator


# ---------------------------------------------------------------------------- #
#                            MAIN STREAMLINE FUCNTION                          #
# ---------------------------------------------------------------------------- #

def main_streamline(
    code_filepath,
    from_language,
    to_language,
    generative_model,
    output_code_filepath
):
    """
    main_streamline -- Streamline the end-to-end process of the Codeslator 
    project
    """
    # Read the code from file
    code_to_translate = read_input_file(filepath=code_filepath)

    # Set up system message and user prompt
    system_msg = get_system_message(
        from_language=from_language,
        to_language=to_language
    )
    user_prompt = get_user_prompt(
        code_to_translate=code_to_translate,
        from_language=from_language,
        to_language=to_language
    ) 

    # Generate translated code
    translated_code = get_model_translator(
        model_type=generative_model,
        system_message=system_msg,
        user_prompt=user_prompt
    )

    # Process output code
    processed_translated_code = process_output_code(code_string=translated_code)

    # Write output code to file
    write_output_file(
        filepath=output_code_filepath,
        output=processed_translated_code
    )


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
    code_filepath = args.file
    from_language = args.from_language
    to_language = args.to_language
    default_model_type = "gpt-4o"
    generative_model = str(args.model) if args.model else default_model_type
    code_file_extension = get_file_extension(to_language.lower())
    output_filepath = "./files/result_code" + code_file_extension

    # Codeslator streamline
    main_streamline(
        code_filepath=code_filepath,
        from_language=from_language,
        to_language=to_language,
        generative_model=generative_model,
        output_code_filepath=output_filepath
    )


# ---------------------------------------------------------------------------- #
#                                 MAIN EXECUTION                               #
# ---------------------------------------------------------------------------- #

if __name__ == "__main__":
    main()