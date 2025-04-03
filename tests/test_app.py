from unittest.mock import patch
import sys
from my_tkinter_app.app import main
import pytest

@patch('my_tkinter_app.controller.main_controller.MainController.run')
def test_main_no_args(mock_run):
    sys.argv = ['app']
    main()
    mock_run.assert_called_once()

def test_main_version_arg():
    sys.argv = ['app', '--version']
    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == 0