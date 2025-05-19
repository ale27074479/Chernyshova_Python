import pytest
from string_utils import StringUtils


@pytest.fixture
def string_utils():
    return StringUtils()


# === capitalize() ===
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),          # Базовый случай
    ("hello world", "Hello world"), # С пробелом
    ("python", "Python"),          # Одно слово
    ("", ""),                      # Пустая строка (граничный случай)
    ("   ", "   "),                # Пробелы (граничный случай)
    ("123abc", "123abc"),          # Цифры + буквы (граничный случай)
])
def test_capitalize(string_utils, input_str, expected):
    """Тестирует базовые и граничные случаи для capitalize()"""
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.xfail(raises=AttributeError, reason="Bug #1: Should raise AttributeError for None")
def test_capitalize_with_none(string_utils):
    """Проверяет обработку None в capitalize()"""
    with pytest.raises(AttributeError, match="Arguments cannot be None"):
        string_utils.capitalize(None)


# === trim() ===
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),      # Удаление начальных пробелов
    ("  hello  ", "hello  "),     # Пробелы только слева
    ("no_spaces", "no_spaces"),   # Нет пробелов
    ("", ""),                     # Пустая строка (граничный случай)
    (" ", ""),                    # Один пробел (граничный случай)
    ("\t\nleading", "leading"),   # Непечатаемые символы
])
def test_trim(string_utils, input_str, expected):
    """Тестирует базовые и граничные случаи для trim()"""
    assert string_utils.trim(input_str) == expected


@pytest.mark.xfail(raises=AttributeError, reason="Bug #1: Should raise AttributeError for None")
def test_trim_with_none(string_utils):
    """Проверяет обработку None в trim()"""
    with pytest.raises(AttributeError, match="Arguments cannot be None"):
        string_utils.trim(None)


# === contains() ===
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True),       # Содержит символ
    ("SkyPro", "U", False),      # Не содержит символ
    ("123", "2", True),          # Цифры
    ("", "a", False),            # Пустая строка (граничный случай)
    (" ", " ", True),            # Пробел
    pytest.param("SkyPro", "Sky", False, marks=pytest.mark.xfail(reason="Bug #2: Should check single chars only")),
])
def test_contains(string_utils, string, symbol, expected):
    """Тестирует базовые и граничные случаи для contains()"""
    assert string_utils.contains(string, symbol) == expected


@pytest.mark.parametrize("string, symbol", [
    (None, "a"),   # None вместо строки
    ("abc", None),  # None вместо символа
])
def test_contains_with_none(string_utils, string, symbol):
    """Проверяет обработку None в contains()"""
    with pytest.raises(AttributeError, match="Arguments cannot be None"):
        string_utils.contains(string, symbol)


# === delete_symbol() ===
@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),      # Удаление символа
    ("Hello World", "l", "Heo Word"), # Несколько вхождений
    ("12345", "3", "1245"),        # Цифры
    ("SkyPro", "Z", "SkyPro"),     # Символ отсутствует
    ("", "a", ""),                 # Пустая строка (граничный случай)
    (" ", " ", ""),                # Пробел (граничный случай)
])
def test_delete_symbol(string_utils, string, symbol, expected):
    """Тестирует базовые и граничные случаи для delete_symbol()"""
    assert string_utils.delete_symbol(string, symbol) == expected


@pytest.mark.parametrize("string, symbol", [
    (None, "a"),   # None вместо строки
    ("abc", None),  # None вместо символа
])
def test_delete_symbol_with_none(string_utils, string, symbol):
    """Проверяет обработку None в delete_symbol()"""
    with pytest.raises(AttributeError, match="Arguments cannot be None"):
        string_utils.delete_symbol(string, symbol)