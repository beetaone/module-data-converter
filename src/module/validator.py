"""
Validates whether the incoming data has an acceptable type and structure.

Edit this file to verify data expected by you module.
"""

from logging import getLogger
import struct

log = getLogger("validator")


def data_validation(data: any) -> str:
    """
    Validate incoming data i.e. by checking if it is of type dict or list.
    Function description should not be modified.

    Args:
        data (any): Data to validate.

    Returns:
        str: Error message if error is encountered. Otherwise returns None.

    """

    log.debug("Validating ...")

    try:
        # YOUR CODE HERE

        allowed_data_types = [dict]

        if not type(data) in allowed_data_types:
            return f"Detected type: {type(data)} | Supported types: {allowed_data_types} | invalid!"

        return None

    except Exception as e:
        return f"Exception when validating module input data: {e}"


def is_hex(str_value):
    if str_value.startswith("0x"):
        str_value_0x = str_value[2:]
        return not set(str_value_0x) - set("ABCDEFabcdef0123456789")
    else:
        return not set(str_value) - set("ABCDEFabcdef0123456789")


def is_ieee754_float(value: bytes):
    try:
        struct.unpack("f", value)
        return True
    except TypeError:
        return False


def int_type(value):
    if type(value) == int:
        return True
    return False


def iee754_float_type(value):
    if type(value) == bytes and is_ieee754_float():
            return True
    return False


def text_string_type(value):
    if type(value) == str:
        return True
    return False


def hex_string_type(value):
    if type(value) == str and is_hex(value):
            return True
    return False


def is_correct_data_type(fromtype, value):
    types_validator = {
        "int": int_type(value),
        "iee754 float": iee754_float_type(value),
        "text": text_string_type(value),
        "hex": hex_string_type(value),
    }

    return types_validator.get(fromtype, "Mismatching input type")
