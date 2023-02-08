from seasons import check_birth
import pytest

def test_letter():
    with pytest.raises(Exception) as e_info:
        check_birth("cat") == sys.exit()

def test_date():
    with pytest.raises(Exception) as e_info:
        check_birth("January 1, 1990") == sys.exit()