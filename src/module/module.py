"""
This file implements module's main logic.
Data processing should happen here.

Edit this file to implement your module.
"""
from os import getenv
from logging import getLogger
from module.converter import *
from api.send_data import send_data
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
        data_to_convert = detect_input(getenv('INPUT_KEY'), received_data)
        conversion = str("from " + getenv('FROM_TYPE') + " to " + getenv('TO_TYPE'))
        print("data to convert ", data_to_convert)
        if (data_type_validator(getenv('FROM_TYPE'), data_to_convert)):
            #  update the input dictionary (json) with the new value after the conversion
            set_in_dict(received_data, getenv('INPUT_KEY').split('.'), any_conversion(conversion, data_to_convert))
        print("data output  ", received_data)

        send_error = send_data(received_data)
        if send_error:
            log.error(send_error)
        else:
            log.debug("Data sent.")

    except Exception as e:
        return None, f"Exception in the module business logic: {e}"
