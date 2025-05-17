class StringUtils:
    """
    Класс с полезными утилитами для обработки и анализа строк
    """

    def capitalize(self, string: str) -> str:
        """
        Принимает на вход текст, делает первую букву заглавной
        и возвращает этот же текст
        """
        if string is None:
            raise AttributeError("Input cannot be None")
        return string.capitalize()

    def trim(self, string: str) -> str:
        """
        Принимает на вход текст и удаляет пробелы в начале, если они есть
        """
        if string is None:
            raise AttributeError("Input cannot be None")
        whitespace = " "
        while string.startswith(whitespace):
            string = string.removeprefix(whitespace)
        return string

    def contains(self, string: str, symbol: str) -> bool:
        """
        Возвращает `True`, если строка содержит искомый символ
        и `False` - если нет
        """
        if string is None or symbol is None:
            raise AttributeError("Arguments cannot be None")
        return symbol in string

    def delete_symbol(self, string: str, symbol: str) -> str:
        """
        Удаляет все подстроки из переданной строки
        """
        if string is None or symbol is None:
            raise AttributeError("Arguments cannot be None")
        return string.replace(symbol, "")
