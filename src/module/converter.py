from functools import reduce
import operator
import struct


def is_hex(str_value):
    if str_value.startswith("0x"):
        str_value_0x = str_value[2:]
        return not set(str_value_0x) - set("ABCDEFabcdef0123456789")
    else:
        return not set(str_value) - set("ABCDEFabcdef0123456789")


def is_ieee754_float(value: bytes):
    try:
        struct.unpack('f', value)
        return True
    except TypeError:
        return False


def detect_input(input: str, data):
    list_keys = input.split('.')
    for key in list_keys:
        data = data[key]
    return(data)


def int_type(value):
    if type(value) == int:
        return True
    return False


def iee754_float_type(value):
    if type(value) == bytes:
        if (is_ieee754_float()):
            return True
        return False


def text_string_type(value):
    if type(value) == str:
        return True
    return False


def hex_string_type(value):
    if type(value) == str:
        if is_hex(value):
            return True
        return False


def data_type_validator(fromtype, value):
    types_validator = {
        'int': int_type(value),
        "iee754 float": iee754_float_type(value),
        "text": text_string_type(value),
        "hex": hex_string_type(value),
    }

    return types_validator.get(fromtype, "Mismatching input type")


def from_int_to_ieee754_float(value: int):
    return struct.pack("f", value)


def from_int_to_text(value: int):
    return str(value)


def from_int_to_hex(value: int):
    return hex(value)


def from_ieee754_float_to_int(value: bytes):
    return int(struct.unpack('f', value)[0])


def from_ieee754_float_to_text(value: bytes):
    return str(struct.unpack('f', value)[0])


def from_ieee754_float_to_hex(value: bytes):
    return hex(from_ieee754_float_to_int(value))


def from_text_to_int(value: str):
    return int(value)


def from_text_to_ieee754_float(value: str):
    return struct.pack("f", float(value))


def from_text_to_hex(value: str):
    return value.encode('utf-8').hex()


def from_hex_to_int(value: str):
    return int(value, 16)


def from_hex_to_ieee754_float(value: str):
    return from_text_to_ieee754_float(str(from_hex_to_int(value)))


def from_hex_to_text(value: str):
    return str(from_hex_to_int(value))


def any_conversion(conversion, value):
    print(conversion)
    from_type_to_type = {
        "from int to ieee754 float": from_int_to_ieee754_float,
        "from int to text": from_int_to_text,
        "from int to hex": from_int_to_hex,
        "from ieee754 float to int": from_ieee754_float_to_int,
        "from ieee754 float to text": from_ieee754_float_to_text,
        "from ieee754 float to hex": from_ieee754_float_to_hex,
        "from text to int": from_text_to_int,
        "from text to ieee754 float": from_text_to_ieee754_float,
        "from text to hex": from_text_to_hex,
        "from hex to int": from_hex_to_int,
        "from hex to ieee754 float": from_hex_to_ieee754_float,
        "from hex to text": from_hex_to_text,
    }
    if conversion in from_type_to_type:
        return from_type_to_type.get(conversion)(value)
    return "no possible conversation"


def get_from_dict(data_dict, map_list):
    return reduce(operator.getitem, map_list, data_dict)


def set_in_dict(data_dict, map_list, value):
    get_from_dict(data_dict, map_list[:-1])[map_list[-1]] = value
