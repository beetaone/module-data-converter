"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""

from os import getenv
from logging import getLogger
from module.converter import convert
from module.validator import is_correct_data_type
from functools import reduce
import operator

log = getLogger("module")


def module_main(received_data: any) -> [any, str]:
    """
    Process received data by implementing module's main logic.
    Function description should not be modified.

    Args:
        received_data (any): Data received by module and validated.

    Returns:
        any: Processed data that are ready to be sent to the next module or None if error occurs.
        str: Error message if error occurred, otherwise None.

    """

    log.debug("Processing ...")

    try:
        data_to_convert = get_from_dict(received_data, getenv("INPUT_KEY").split("."))
        log.debug(f"data to convert: {data_to_convert}")
        if not is_correct_data_type(data_to_convert):
            err_msg = (
                f"The value to convert ({data_to_convert}) has an unsupported type. Expected: "
                + getenv("FROM_TYPE")
            )
            return None, err_msg

        converted_value = convert(data_to_convert)
        log.debug(f"converted {data_to_convert} to {converted_value}")
        update_dict(received_data, getenv("INPUT_KEY").split("."), converted_value)

        log.debug(f"data output: {received_data}")

        return received_data, None

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"


def get_from_dict(data_dict: dict, keys: list):
    return reduce(operator.getitem, keys, data_dict)


def update_dict(data_dict: dict, keys: list, value):
    get_from_dict(data_dict, keys[:-1])[keys[-1]] = value
