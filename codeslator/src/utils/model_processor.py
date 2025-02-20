# ---------------------------------------------------------------------------- #
# Author: Han-Elliot Phan                                                      #
# Email: hanelliotphan@gmail.com                                               #
#                                                                              #
# Last update: February 20, 2025                                               #
# ---------------------------------------------------------------------------- #

# ---------------------------------------------------------------------------- #
# model_processor.py                                                           #
#                                                                              #
# This file is for processing the model to generate translated code.           #
# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #
#                               IMPORT LIBRARIES                               #
# ---------------------------------------------------------------------------- #

import logging
import os
import sys

from models.gpt4 import gpt4_stream
from models.claude3 import claude3_stream
from utils.code_processor import translate_code_gpt, translate_code_claude
from utils.login import openai_login, anthropic_login


# ---------------------------------------------------------------------------- #
#                          MODEL PROCESSING FUNCTIONS                          #
# ---------------------------------------------------------------------------- #

def get_model_name(model_type):
    """
    get_model_name -- Get the model name from input model type
    """
    models = {
        "gpt-4o": "gpt-4o",
        "claude-3": "claude-3-5-sonnet-20240620"
    }
    if model_type not in models:
        logging.error(msg="[model_processor.py] get_model: The model you have chosen is not currently supported. Please choose from the following options:")
        for model in models.keys():
            logging.info(msg=f"- {model.capitalize()}")
        sys.exit(1)
    return models[model_type]


def get_model_api_key_var(model_type):
    """
    get_model_api_key_var -- Get the mode API key environment variables from 
        the input model type
    """
    model_api_key_vars = {
        "gpt-4o": "OPENAI_API_KEY",
        "claude-3": "ANTHROPIC_API_KEY"
    }
    if model_type not in model_api_key_vars:
        logging.error(msg="[model_processor.py] get_model_api_key_var: The model you have chosen is not currently supported. Please choose from the following options:")
        for model in model_api_key_vars.keys():
            logging.info(msg=f"- {model.capitalize()}")
        sys.exit(1)
    return model_api_key_vars[model_type]


def get_model_api_key(model_type):
    """
    get_model_api_key -- Get the model API key from input model type
    """
    return os.environ.get(get_model_api_key_var(model_type=model_type))


def get_model_client(model_type):
    """
    get_model_client -- Get the model client from input model type
    """
    model_api_key = get_model_api_key(model_type=model_type)
    model_clients =  {
        "gpt-4o": openai_login(api_key=model_api_key),
        "claude-3": anthropic_login(api_key=model_api_key)
    }
    if model_type not in model_clients:
        logging.error(msg="[model_processor.py] get_model_client: The model you have chosen is not currently supported. Please choose from the following options:")
        for model in model_clients.keys():
            logging.info(msg=f"- {model.capitalize()}")
        sys.exit(1)
    return model_clients[model_type]


def get_model_stream(model_type, system_message, user_prompt):
    """
    get_model_stream -- Get the model stream from input model type
    """
    model_client = get_model_client(model_type=model_type)
    model_name = get_model_name(model_type=model_name)
    model_streams = {
        "gpt-4o": gpt4_stream(
            openai_client=model_client,
            gpt4_model=model_name,
            system_message=system_message,
            user_prompt=user_prompt
        ),
        "claude-3": claude3_stream(
            anthropic_client=model_client,
            claude_model=model_name,
            system_message=system_message,
            user_prompt=user_prompt
        )
    }
    if model_type not in model_streams:
        logging.error(msg="[model_processor.py] get_model_stream: The model you have chosen is not currently supported. Please choose from the following options:")
        for model in model_streams.keys():
            logging.info(msg=f"- {model.capitalize()}")
        sys.exit(1)
    return model_streams[model_type]


def get_model_translator(model_type, system_message, user_prompt):
    """
    get_model_translator -- Get the model translator based on model type
    """
    stream = get_model_stream(
        model_type=model_type,
        system_message=system_message,
        user_prompt=user_prompt
    )
    model_translators = {
        "gpt-4o": translate_code_gpt(gpt_stream=stream),
        "claude-3": translate_code_claude(claude_stream=stream)
    }
    if model_type not in model_translators:
        logging.error(msg="[model_processor.py] get_model_stream: The model you have chosen is not currently supported. Please choose from the following options:")
        for model in model_translators.keys():
            logging.info(msg=f"- {model.capitalize()}")
        sys.exit(1)
    return model_translators[model_type]