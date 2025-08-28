import pytest
from Mocker import AddThemNumbers

def test_AddThemNumbers_valid(mocker):
    mock_validate = mocker.patch('Mocker._validate_input')
    
    result = AddThemNumbers(5, 3)
    

    mock_validate.assert_called_once_with(5, 3)
    assert result == 8

def test_AddThemNumbers_invalid_mocked(mocker):

    mocker.patch('Mocker._validate_input', side_effect=TypeError("Mocked error"))

    with pytest.raises(TypeError, match="Mocked error"):
        AddThemNumbers(1, 2)
