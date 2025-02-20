# ---------------------------------------------------------------------------- #
# Author: Han-Elliot Phan                                                      #
# Email: hanelliotphan@gmail.com                                               #
#                                                                              #
# Last update: February 19, 2025                                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# code_processor.py                                                            #
#                                                                              #
# This file is to process the code to translate using the supported models     #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                         CODE PROCESSING FUNCTIONS                            #
# ---------------------------------------------------------------------------- #

def get_system_message(from_language, to_language):
    """
    get_system_message -- Return system message for message prompt
    """
    system_msg = f"""
    You are an assistant that translates code from {from_language.capitalize()} into high-performance {to_language.capitalize()} code.
    The response should only include {to_language.capitalize()} code. Do not include any other text or explanation.
    The {to_language.capitalize()} code should be optimized for performance in the fastest possible time.
    """
    return system_msg


def get_user_prompt(code_to_translate, from_language, to_language):
    """
    get_user_prompt -- Return user prompt for message prompt
    """
    user_prompt = f"""
    Rewrite this {from_language.capitalize()} code into {to_language.capitalize()} with the fastest possible implementation that produces identical output in the least amount of time and number of lines.
    The response should only include {to_language.capitalize()} code. Do not include any other text or explanation.
    Pay attention to number types to ensure no overflows, and remember to include all necessary packages related to the {to_language.capitalize()} code.
    The code has to be able to run with Mac M1 and such.
    
    Here is the {from_language.capitalize()} code:

    ```
    {code_to_translate}
    ```
    """
    return user_prompt


def translate_code_gpt(gpt_stream):
    """
    translate_code_gpt -- Translate code using the developed GPT stream
    """
    result = ""
    for chunk in gpt_stream:
        fragment = chunk.choices[0].delta.content or ""
        result += fragment
    return result


def translate_code_claude(claude_stream):
    """
    translate_code_claude -- Translate code using the developed Claude stream
    """
    result = ""
    with claude_stream as stream:
        for text in stream.text_stream:
            result += text
    return result