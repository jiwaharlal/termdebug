from typing import *

# reads quoted token, returns unquoted token and position after closing quote
def parse_quoted_token(msg: str, first_quote: int, end=len(msg)):
    escaped = False
    res = ''
    for i in range(first_quote + 1, end):
        c = msg[i]
        if c == '\\':
            escaped = True
            continue

        if escaped:
            escaped = False
        elif c == '"':
            return res

        res += c

    return res


def parse_locals_msg(msg):
    name_str = '{name="'
    val_str = ',value="'
    arg_str = ',arg="'

    name_idx = msg.find(name_str)
    res = []
    while name_idx != -1:
        vardict = {}
        next_name_idx = msg.find(name_str, name_idx + len(name_str))
        vardict_end = next_name_idx if next_name_idx > 0 else len(msg)
        name = parse_quoted_token(msg, name_idx + len(name_str) - 1, vardict_end)
        vardict['name'] = name

        val_idx = msg.find(val_str, name_idx + len(name_str) + len(name), vardict_end)
        val = '{}' if val_idx == -1 else parse_quoted_token(msg, val_idx + len(val_str) - 1, vardict_end)
        vardict['value'] = val

        name_idx = next_name_idx
        res.append(vardict)

    return res

