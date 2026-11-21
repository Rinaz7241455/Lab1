# Контрольный пример (Фотография 2)
# S = 10000, вклады: 2000, 3000, 5000

total_sum = 10000
contrib_1, contrib_2, contrib_3 = 2000, 3000, 5000

total_contrib = contrib_1 + contrib_2 + contrib_3

share_1 = total_sum * (contrib_1 / total_contrib)
share_2 = total_sum * (contrib_2 / total_contrib)
share_3 = total_sum * (contrib_3 / total_contrib)

print("--- Результаты распределения суммы S ---")
print(f"Общий вклад участников: {total_contrib:.2f}")
print(f"Доля 1-го участника ({contrib_1 / total_contrib * 100:.1f}%): {share_1:.2f}")
print(f"Доля 2-го участника ({contrib_2 / total_contrib * 100:.1f}%): {share_2:.2f}")
print(f"Доля 3-го участника ({contrib_3 / total_contrib * 100:.1f}%): {share_3:.2f}")
