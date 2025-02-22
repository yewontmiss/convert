def convert_units():
    conversions = {
        "1": ("сантиметры в дюймы", lambda x: x / 2.54),
        "2": ("дюймы в сантиметры", lambda x: x * 2.54),
        "3": ("килограммы в фунты", lambda x: x * 2.20462),
        "4": ("фунты в килограммы", lambda x: x / 2.20462),
        "5": ("километры в мили", lambda x: x * 0.621371),
        "6": ("мили в километры", lambda x: x / 0.621371),
    }
    
    while True:
        print("Выберите, что хотите конвертировать:")
        for key, (name, _) in conversions.items():
            print(f"{key}. {name}")
        print("0. Выйти")
        
        choice = input("Введите номер: ").strip()
        if choice == "0":
            print("Выход...")
            break
        
        if choice in conversions:
            try:
                value = float(input("Введите значение: "))
                result = conversions[choice][1](value)
                print(f"Результат: {result:.2f}\n")
            except ValueError:
                print("Ошибка: введите числовое значение.\n")
        else:
            print("Неверный ввод, попробуйте снова.\n")

if __name__ == "__main__":
    convert_units()
