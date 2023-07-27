import parse_messages
import pytest
import pudb

def test_parse_locals():
    msg = '^done,variables=[{name="sol",value="{23}"},{name="msg",value="\\"job done\\""}]'
    expected = [{'name':'sol', 'value':'{23}'}, {'name':'msg', 'value':'"job done"'}]
    # pytest.set_trace()
    # pudb.set_trace()

    assert parse_messages.parse_locals_msg(msg) == expected

    msg = '^done,variables=[{name="i",value="0"},{name="this",arg="1",value="0x7f"},{name="n",arg="1",value="1"},{name="headID",arg="1",value="0"},{name="manager",arg="1",value="{-1}"},{name="informTime",arg="1",value="{0}"},{name="leaves"},{name="num_subordinates",value="{215, 0, 1}"},{name="times",value="{7, 1, 0}"}]'
    expected = [
            {'name':'i', 'value':'0'},
            {'name':'this', 'value':'0x7f'},
            {'name':'n', 'value':'1'},
            {'name':'headID', 'value':'0'},
            {'name':'manager', 'value':'{-1}'},
            {'name':'informTime', 'value':'{0}'},
            {'name':'leaves', 'value':'{}'},
            {'name':'num_subordinates', 'value':'{215, 0, 1}'},
            {'name':'times', 'value':'{7, 1, 0}'} ]

    assert parse_messages.parse_locals_msg(msg) == expected

    msg = ' ^done,variables=[{name="m",value="{[3] = \\"th\\\"ree\\", [2] = \\"two\\", [1] = \\"one\\"}"}"}]'
    expected = [{'name':'m', 'value':'{[3] = "th\"ree", [2] = "two", [1] = "one"}'}]
    assert parse_messages.parse_locals_msg(msg) == expected

def test_parse_quoted_token():
    # msg = R'"\"job done\""}]'
    msg = '"\\"job done\\""}]'
    expected = '"job done"'
    # pytest.set_trace()
    assert parse_messages.parse_quoted_token(msg, 0) == expected
