"""
Validates whether the incoming data has an acceptable type and structure.

Edit this file to verify data expected by you module.
"""

from os import getenv
from logging import getLogger
import struct


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


def is_hex(value):
    if type(value) != str:
        return False
    if value.startswith("0x"):
        value = value[2:]
    return not set(value) - set("ABCDEFabcdef0123456789")


def is_ieee754_float(value: bytes):
    if type(value) != bytes:
        return False
    try:
        struct.unpack("f", value)
        return True
    except TypeError:
        return False


def is_int(value):
    return type(value) == int


def is_text(value):
    return type(value) == str


types_validator = {
    "int": is_int,
    "iee754 float": is_ieee754_float,
    "text": is_text,
    "hex": is_hex,
}

log = getLogger("validator")

if getenv("FROM_TYPE") not in types_validator:
    log.error("Cannot covert from type " + getenv("FROM_TYPE"))
    exit(1)
is_correct_data_type = types_validator[getenv("FROM_TYPE")]
