#!/usr/bin/python3
"""
function to append to file
"""


def append_write(filename="", text=""):
    """
    append to file
    Args:
        filename (str): name of file
        text (str): text to append
        Return: the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        data = file.write(text)
        return data
