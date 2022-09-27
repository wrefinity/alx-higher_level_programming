#!/usr/bin/python3
"""
function to write to file
"""


def write_file(filename="", text=""):
    """ use utf-8 encoding & write to file
        Args:
            filename (str): name of file.
            text (str): text to be written.
            Return: the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        data = file.write(text)
        return(data)
