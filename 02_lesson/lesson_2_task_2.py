def is_year_leap(year):
    """Определяет, является ли год високосным.
    
    Args:
        year (int): Год для проверки.
        
    Returns:
        bool: True если год високосный, иначе False.
    """
    return year % 4 == 0


# Пример вызова функции
test_year = 2028
result = is_year_leap(test_year)
print(f"год {test_year}: {result}")

# Дополнительные примеры (для проверки)
print(f"год 2023: {is_year_leap(2023)}")
print(f"год 2000: {is_year_leap(2000)}")
print(f"год 1900: {is_year_leap(1900)}")