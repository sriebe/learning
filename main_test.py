import pytest
from io import StringIO
import sys
from main import main

# test_main.py


def test_main_output(capsys):
    # Capture the output of the main function
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello\n"