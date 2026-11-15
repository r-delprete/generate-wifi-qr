def escape_wifi(value: str) -> str:
    for char in ('\\', ';', ',', '"'):
        value = value.replace(char, '\\' + char)
    return value
