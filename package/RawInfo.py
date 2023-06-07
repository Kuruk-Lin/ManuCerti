import os
import socket

Verify_XPath = '//android.widget.EditText'


def get_user():
    return socket.gethostname().split("-")[0]

