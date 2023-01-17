import struct


def from_int_to_ieee754_float(value: int):
    return struct.pack("f", value)


def from_int_to_text(value: int):
    return str(value)


def from_int_to_hex(value: int):
    return hex(value)


def from_ieee754_float_to_int(value: bytes):
    return int(struct.unpack("f", value)[0])


def from_ieee754_float_to_text(value: bytes):
    return str(struct.unpack("f", value)[0])


def from_ieee754_float_to_hex(value: bytes):
    return hex(from_ieee754_float_to_int(value))


def from_text_to_int(value: str):
    return int(value)


def from_text_to_ieee754_float(value: str):
    return struct.pack("f", float(value))


def from_text_to_hex(value: str):
    return value.encode("utf-8").hex()


def from_hex_to_int(value: str):
    return int(value, 16)


def from_hex_to_ieee754_float(value: str):
    return from_text_to_ieee754_float(str(from_hex_to_int(value)))


def from_hex_to_text(value: str):
    return str(from_hex_to_int(value))


def convert(conversion, value):
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
