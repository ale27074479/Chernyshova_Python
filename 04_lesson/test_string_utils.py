import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


def test_capitalize_positive(string_utils):
    assert string_utils.capitalize("skypro") == "Skypro"
    assert string_utils.capitalize("hello world") == "Hello world"
    assert string_utils.capitalize("python") == "Python"


def test_capitalize_negative(string_utils):
    assert string_utils.capitalize("") == ""
    assert string_utils.capitalize("   ") == "   "
    assert string_utils.capitalize("123abc") == "123abc"


def test_capitalize_with_none(string_utils):
    with pytest.raises(AttributeError):
        string_utils.capitalize(None)


def test_trim_positive(string_utils):
    assert string_utils.trim("   skypro") == "skypro"
    assert string_utils.trim("  hello  ") == "hello  "
    assert string_utils.trim("no_spaces") == "no_spaces"


def test_trim_negative(string_utils):
    assert string_utils.trim("") == ""
    assert string_utils.trim(" ") == ""


def test_trim_with_none(string_utils):
    with pytest.raises(AttributeError):
        string_utils.trim(None)


def test_contains_positive(string_utils):
    assert string_utils.contains("SkyPro", "S") is True
    assert string_utils.contains("SkyPro", "k") is True
    assert string_utils.contains("123", "2") is True


def test_contains_negative(string_utils):
    assert string_utils.contains("SkyPro", "U") is False
    assert string_utils.contains("", "a") is False
    assert string_utils.contains(" ", " ") is True


def test_contains_with_none(string_utils):
    with pytest.raises(AttributeError):
        string_utils.contains(None, "a")
    with pytest.raises(AttributeError):
        string_utils.contains("abc", None)


def test_delete_symbol_positive(string_utils):
    assert string_utils.delete_symbol("SkyPro", "k") == "SyPro"
    assert string_utils.delete_symbol("Hello World", "l") == "Heo Word"
    assert string_utils.delete_symbol("12345", "3") == "1245"


def test_delete_symbol_negative(string_utils):
    assert string_utils.delete_symbol("SkyPro", "Z") == "SkyPro"
    assert string_utils.delete_symbol("", "a") == ""
    assert string_utils.delete_symbol(" ", " ") == ""


def test_delete_symbol_with_none(string_utils):
    with pytest.raises(AttributeError):
        string_utils.delete_symbol(None, "a")
    with pytest.raises(AttributeError):
        string_utils.delete_symbol("abc", None)
