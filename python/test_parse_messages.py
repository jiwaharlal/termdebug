import parse_messages

def test_parse_locals():
    msg = '^done,variables=[{name="sol",value="{23}"},{name="msg",value="\"job done\""}]'
    expected = [{'name':'sol', 'value':'{23}'}, {'name':'msg', 'value':'"job done"'}]
    assert parse_messages.parse_locals_msg(msg) == expected

    msg = '^done,variables=[{name="i",value="0"},{name="this",arg="1",value="0x7f"},{name="n",arg="1",value="1"},{name="headID",arg="1",value="0"},{name="manager",arg="1",value="{-1}"},{name="informTime",arg="1",value="{0}"},{name="leaves"},{name="num_subordinates",value="{215, 0, 1}"},{name="times",value="{7, 1, 0}"}]'
    expected = [
            {'name':'i', 'value':'0'},
            {'name':'this', 'value':'0x7f'},
            {'name':'n', 'value':'1'},
            {'name':'headID', 'value':'0'},
            {'name':'manager', 'value':'{-1}'},
            {'name':'informTime', 'value':'{0}'},
            {'name':'leaves'},
            {'name':'num_subordinates', 'value':'{215, 0, 1}'},
            {'name':'times', 'value':'{7, 1, 0}'} ]

    assert parse_messages.parse_locals_msg(msg) == expected

