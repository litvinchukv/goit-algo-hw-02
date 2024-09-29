from collections import deque

def is_palindrome(s: str) -> bool:
    # Очищуємо рядок: видаляємо пробіли та приводимо до нижнього регістру
    cleaned_str = ''.join(char.lower() for char in s if char.isalnum())

    # Додаємо символи очищеного рядка до двосторонньої черги
    char_deque = deque(cleaned_str)

    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        # Видаляємо і порівнюємо символи з початку і кінця черги
        if char_deque.popleft() != char_deque.pop():
            return False  # Якщо знайшли різницю, рядок не є паліндромом

    return True  # Якщо всі символи збігаються, рядок є паліндромом

# Приклад використання:
input_str = "A man a plan a canal Panama"
if is_palindrome(input_str):
    print(f'"{input_str}" є паліндромом.')
else:
    print(f'"{input_str}" не є паліндромом.')
