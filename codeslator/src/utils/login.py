# ---------------------------------------------------------------------------- #
# Author: Han-Elliot Phan                                                      #
# Email: hanelliotphan@gmail.com                                               #
#                                                                              #
# Last update: February 19, 2025                                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# login.py                                                                     #
#                                                                              #
# This file is for setting up Anthropic & OpenAI login using                   # 
# ANTHROPIC_API_KEY and OPENAI_API_KEY environment variables.                  #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                               IMPORT LIBRARIES                               #
# ---------------------------------------------------------------------------- #

import logging
import sys

from anthropic import Anthropic
from openai import OpenAI


# ---------------------------------------------------------------------------- #
#                                LOGIN FUNCTIONS                               #
# ---------------------------------------------------------------------------- #

def openai_login(api_key):
    """
    openai_login -- Log in to OpenAI interface using OpenAI API key

    Documentation: https://platform.openai.com/docs/quickstart
    """
    openai_client = OpenAI(api_key=api_key)
    try:
        openai_client.models.list()
        logging.info(msg="[login.py] openai_login: Successfully logged in to OpenAI")
    except Exception as e:
        logging.critical(msg=f"[login.py] openai_login: Cannot log in to OpenAI. Error message: {e}")
        sys.exit(-1)
    return openai_client


def anthropic_login(api_key):
    """
    anthropic_login -- Log in to Anthropic interface using Anthropic API key

    Documentation: https://docs.anthropic.com/en/api/getting-started#authentication
    """
    anthropic_client = Anthropic(api_key=api_key)
    try:
        anthropic_client.models.list()
        logging.info(msg="[login.py] anthropic_login: Successfully logged in to Anthropic")
    except Exception as e:
        logging.critical(msg=f"[login.py] anthropic_login: Cannot log in to Anthropic. Error message: {e}")
        sys.exit(-1)
    return anthropic_client