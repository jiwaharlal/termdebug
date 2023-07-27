from typing import *

msg = '^done,variables=[{name="sol",value="{<No data fields>}"},{name="msg",value="\"job done\""},{name="test_data",value="std::vector of length -2932031008512, capacity -2932031008256 = {std::tuple containing = {[0] = std::vector of length -164, capacity -164 = {<error reading variable: Cannot access memory at address 0x291>"}]'

msg = '^done,variables=[{name="expected",value="@0x7f: 17"},{name="vals",value="{1, 2, 4, 5, 7, 8}"},{name="msg",value="\"job done\""},{name="m",value="{[3] = \"th\\\"ree\", [2] = \"two\", [1] = \"one\"}"},{name="test_data",value="{{[0] = {0, 1, 0}, [1] = 1}, {[0] = {0, 2, 1, 0}, [1] = 1}, {[0] = {0, 10, 5, 2}, [1] = 1}}"}]'

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

def parse_locals_msg_old(msg):
    msg = msg[msg.index('['):]
    name_str = '{name="'
    val_str = '",value="'
    arg_str = '",arg="'
    name_idx = msg.find(name_str)
    res = []
    while name_idx != -1:
        next_name_idx = msg.find(name_str, start=name_idx + len(name_str))

        value_idx = msg.find(val_str, name_idx + len(name_str))
        name = msg[name_idx + len(name_str) : value_idx]

        name_idx = msg.find(name_str, value_idx)
        end_idx = name_idx - 3 if name_idx != -1 else -3

        value = msg[value_idx + len(val_str) : end_idx]
        # un-escape
        escape = False
        val = ''
        for c in value:
            if escape:
                val += c
                escape = False
                continue
            if c == '\\':
                escape = True
                continue
            val += c

        res.append({'name': name, 'value': val})

    return res

