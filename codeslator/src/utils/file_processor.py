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

import openai
import logging
import sys


# ---------------------------------------------------------------------------- #
#                          FILE PROCESSING FUNCTIONS                           #
# ---------------------------------------------------------------------------- #

def generate_output_file(filepath, output):
    """
    generate_output_file -- Write output to file
    """
    with open(filepath, "w") as f:
        f.write(output)