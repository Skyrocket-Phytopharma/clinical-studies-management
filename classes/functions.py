def convert_to_int(s):
    try:
        ret = int(s)
    except:
        ret = 0
    return ret


def parse(s, divider):
    if s is None:
        return None
    elif s == "":
        return None
    else:
        ret = s.split(divider)
        return ret
