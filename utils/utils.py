def convert_to_int(s):
    try:
        ret = int(s)
    except Exception as _:
        ret = 0
    return ret


def parse(s, divider):
    if s is None or s == "":
        return None
    else:
        ret = s.split(divider)
        return ret
