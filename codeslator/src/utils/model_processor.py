import logging
import sys


def get_model(model_type):
    """
    get_model -- Get the exact model from input model type
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