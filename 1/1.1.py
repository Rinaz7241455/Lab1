# Лабораторная работа № 1. Вариант 8: «Доли»
# Разделение суммы S между тремя участниками пропорционально их вкладам

def main() -> None:
    # Ввод общей суммы и вкладов каждого из трёх участников с клавиатуры
    total_sum: float = float(input("Введите общую сумму S: "))
    contrib_1: float = float(input("Введите вклад 1-го участника: "))
    contrib_2: float = float(input("Введите вклад 2-го участника: "))
    contrib_3: float = float(input("Введите вклад 3-го участника: "))

    # Вычисление суммарного вклада всех участников
    total_contrib: float = contrib_1 + contrib_2 + contrib_3

    if total_contrib <= 0:
        print("Ошибка: общий вклад должен быть больше нуля.")
        return

    # Вычисление доли каждого участника пропорционально его вкладу
    share_1: float = total_sum * (contrib_1 / total_contrib)
    share_2: float = total_sum * (contrib_2 / total_contrib)
    share_3: float = total_sum * (contrib_3 / total_contrib)

    # Вывод результатов в читаемом виде с пояснениями
    print("\n--- Результаты распределения суммы S ---")
    print(f"Общий вклад участников: {total_contrib:.2f}")
    print(f"Доля 1-го участника ({contrib_1 / total_contrib * 100:.1f}%): {share_1:.2f}")
    print(f"Доля 2-го участника ({contrib_2 / total_contrib * 100:.1f}%): {share_2:.2f}")
    print(f"Доля 3-го участника ({contrib_3 / total_contrib * 100:.1f}%): {share_3:.2f}")


if __name__ == "__main__":
    main()
