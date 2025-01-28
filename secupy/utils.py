import logging

def validate_input(data, expected_type):
    if not isinstance(data, expected_type):
        logging.error(f"Expected {expected_type}, but got {type(data)}")
        raise TypeError(f"Expected {expected_type}, but got {type(data)}")
