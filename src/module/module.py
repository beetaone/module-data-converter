"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""

from os import getenv
from logging import getLogger
from module.converter import convert
from module.validator import is_correct_data_type
from api.send_data import send_data
from functools import reduce
import operator

log = getLogger("module")

conversion = "from " + getenv("FROM_TYPE") + " to " + getenv("TO_TYPE")
log.info("Converting " + conversion)


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
        if not is_correct_data_type(getenv("FROM_TYPE"), data_to_convert):
            err_msg = f"The value to convert has an unsupported type: {data_to_convert}. Supported types are int, ieee754 float, text, hex"
            log.error(err_msg)
            return None, err_msg

        converted_value = convert(conversion, data_to_convert)
        log.debug(f"converted {data_to_convert} to {converted_value}")
        update_dict(received_data, getenv("INPUT_KEY").split("."), converted_value)

        log.debug(f"data output: {received_data}")

        send_error = send_data(received_data)
        if send_error:
            log.error(send_error)
        else:
            log.debug("Data sent.")

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"


def get_from_dict(data_dict: dict, keys: list):
    return reduce(operator.getitem, keys, data_dict)


def update_dict(data_dict: dict, keys: list, value):
    get_from_dict(data_dict, keys[:-1])[keys[-1]] = value
