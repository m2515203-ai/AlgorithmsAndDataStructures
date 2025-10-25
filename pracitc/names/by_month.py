import pandas as pd
from matplotlib import pyplot as plt

df_man_names = pd.read_csv('Number_of_names_man.csv', sep=';', skiprows=[1])
df_woman_names = pd.read_csv('Number_of_names_woman.csv', sep=';', skiprows=[1])

# Получаем топ-10 самых популярных имен за весь период
overall_top = df_man_names.groupby('Name')['NumberOfPersons'].sum().nlargest(10)

# =============================================================================
# ГРАФИК 1: Столбчатая диаграмма - Топ-10 популярных имен за весь период
# =============================================================================
fig1, ax1 = plt.subplots(figsize=(14, 8))

colors = plt.cm.Set3(range(10))
bars = ax1.bar(overall_top.index, overall_top.values, color=colors, edgecolor='black', linewidth=1.5)

# Добавляем значения на столбцы
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2., height,
             f'{int(height):,}',
             ha='center', va='bottom', fontsize=11, fontweight='bold')

ax1.set_xlabel('Имя', fontsize=14, fontweight='bold')
ax1.set_ylabel('Количество человек', fontsize=14, fontweight='bold')
ax1.set_title('Топ-10 самых популярных мужских имен за весь период',
              fontsize=16, fontweight='bold', pad=20)
ax1.grid(True, alpha=0.3, axis='y')
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.tight_layout()
plt.show()

# =============================================================================
# ГРАФИК 2: Круговая диаграмма - Доля топ-10 имен
# =============================================================================
fig2, ax2 = plt.subplots(figsize=(12, 10))

colors = plt.cm.Set3(range(10))
wedges, texts, autotexts = ax2.pie(overall_top.values,
                                   labels=overall_top.index,
                                   autopct='%1.1f%%',
                                   startangle=90,
                                   colors=colors,
                                   explode=[0.05] * 10,
                                   shadow=True,
                                   textprops={'fontsize': 11, 'fontweight': 'bold'})

ax2.set_title('Распределение топ-10 самых популярных мужских имен',
              fontsize=16, fontweight='bold', pad=20)

# Улучшаем читаемость процентов
for autotext in autotexts:
    autotext.set_color('black')
    autotext.set_fontsize(10)

plt.tight_layout()
plt.show()

# =============================================================================
# ГРАФИК 3: Динамика по годам - Линейный график
# =============================================================================
yearst_names = df_man_names.groupby(['Year', 'Name'])['NumberOfPersons'].sum().reset_index()

fig3, ax3 = plt.subplots(figsize=(16, 8))

for name in overall_top.index:
    # Для каждого имени собираем данные по годам
    name_by_year = yearst_names[yearst_names['Name'] == name].copy()

    # Сортируем по годам
    name_by_year = name_by_year.sort_values('Year')

    # Строим линию
    ax3.plot(name_by_year['Year'], name_by_year['NumberOfPersons'],
             marker='o', linewidth=2.5, label=name, markersize=6)

ax3.set_xlabel('Год', fontsize=14, fontweight='bold')
ax3.set_ylabel('Количество человек', fontsize=14, fontweight='bold')
ax3.set_title('Динамика популярности топ-10 мужских имен по годам',
              fontsize=16, fontweight='bold', pad=20)
ax3.legend(loc='best', fontsize=11, framealpha=0.9)
ax3.grid(True, alpha=0.3)
plt.xticks(rotation=45, fontsize=11)
plt.tight_layout()
plt.show()

# =============================================================================
# ГРАФИК 4: Динамика по месяцам (агрегированные данные)
# =============================================================================
monthly_names = df_man_names.groupby(['Month', 'Name'])['NumberOfPersons'].sum().reset_index()

# Создаем порядок месяцев для правильной сортировки
month_order = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь',
               'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

fig4, ax4 = plt.subplots(figsize=(16, 8))

for name in overall_top.index:
    # Для каждого имени собираем данные по месяцам
    name_by_month = monthly_names[monthly_names['Name'] == name].copy()

    # Сортируем по порядку месяцев
    name_by_month['month_num'] = name_by_month['Month'].map(
        {month: i for i, month in enumerate(month_order)}
    )
    name_by_month = name_by_month.sort_values('month_num')

    # Строим линию
    ax4.plot(name_by_month['Month'], name_by_month['NumberOfPersons'],
             marker='o', linewidth=2.5, label=name, markersize=6)

ax4.set_xlabel('Месяц', fontsize=14, fontweight='bold')
ax4.set_ylabel('Количество человек', fontsize=14, fontweight='bold')
ax4.set_title('Динамика популярности топ-10 мужских имен по месяцам (суммарно)',
              fontsize=16, fontweight='bold', pad=20)
ax4.legend(loc='best', fontsize=11, framealpha=0.9)
ax4.grid(True, alpha=0.3)
plt.xticks(rotation=45, fontsize=11)
plt.tight_layout()
plt.show()

# Выводим таблицу с топ-10
print("\n" + "=" * 60)
print("ТОП-10 САМЫХ ПОПУЛЯРНЫХ МУЖСКИХ ИМЕН ЗА ВЕСЬ ПЕРИОД")
print("=" * 60)
for i, (name, count) in enumerate(overall_top.items(), 1):
    print(f"{i:2d}. {name:15s} - {count:,} человек")
print("=" * 60)
