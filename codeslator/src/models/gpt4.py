# ---------------------------------------------------------------------------- #
# Author: Han-Elliot Phan                                                      #
# Email: hanelliotphan@gmail.com                                               #
#                                                                              #
# Last update: February 19, 2025                                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# gpt4.py                                                                      #  
#                                                                              #
# This file is for setting up the GPT-4 model in order to generate             #
# codes from one programming language to another language.                     #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                             IMPORT LIBRARIES                                 #
# ---------------------------------------------------------------------------- #

import logging
import sys


# ---------------------------------------------------------------------------- #
#                       GPT-4o MODEL SETUP FUNCTIONS                           #
# ---------------------------------------------------------------------------- #

def gpt4_stream(openai_client, gpt4_model, system_message, user_prompt):
    """
    gpt4_stream -- Set up GPT-4o stream model
    """
    stream = None
    try:
        messages = [
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_prompt}
        ]
        stream = openai_client.chat.completions.create(
            model=gpt4_model,
            messages=messages,
            stream=True
        )
    except Exception as e:
        logging.critical(msg=f"[gpt4.py] gpt4_stream: Cannot configure message stream. Error message: {e}")
        sys.exit(-1)
    return stream