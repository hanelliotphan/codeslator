# ---------------------------------------------------------------------------- #
# Author: Han-Elliot Phan                                                      #
# Email: hanelliotphan@gmail.com                                               #
#                                                                              #
# Last update: February 19, 2025                                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# claude3.py                                                                   #
#                                                                              #
# This file is for setting up the Claude 3.5 Sonnet model in order to generate #
# codes from one programming language to another language.                     #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                               IMPORT LIBRARIES                               #
# ---------------------------------------------------------------------------- #

import logging
import sys


# ---------------------------------------------------------------------------- #
#                   CLAUDE 3.5 SONNET MODEL SETUP FUNCTIONS                    #
# ---------------------------------------------------------------------------- #

def claude3_stream(anthropic_client, claude_model, system_message, user_prompt):
    """
    claude3_stream -- Set up Claude 3.5 Sonnet stream model
    """
    stream = None
    try:
        stream = anthropic_client.messages.stream(
            model=claude_model,
            max_tokens=2000,
            system=system_message,
            messages=[{"role": "user", "content": user_prompt}]
        )
    except Exception as e:
        logging.critical(msg=f"[claude3.py] claude3_stream: Cannot configure message stream. Error message: {e}")
        sys.exit(-1)
    return stream