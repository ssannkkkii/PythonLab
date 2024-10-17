time = input('Введіть час засідання: ')
name = input('Введіть назву проблеми: ')
organizator = input('Введіть організатора: ')
num_appliaction = int(input('Введіть кількість заявок: '))
cost_money = float(input('Введіть загальну суму заявок: '))

awerage = cost_money / num_appliaction


text_percent = 'Сьогодні в "%s" буде проходити позачергове засідання комітету з проблем "%s", організоване "%s". Було подано "%s" заявок на загальну суму "%.2f" тис. гривень. Середня вартість проекту склала "%.2f" гривень.' % (time, name, organizator, num_appliaction, cost_money, awerage)

text_format = 'Сьогодні в "{0}" буде проходити позачергове засідання комітету з проблем "{1}", організоване "{2}". Було подано "{3}" заявок на загальну суму "{4:.2f}" тис. гривень. Середня вартість проекту склала "{5:.2f}" гривень.'.format(time, name, organizator, num_appliaction, cost_money, awerage)

text_fstring = f'Сьогодні в "{time}" буде проходити позачергове засідання комітету з проблем "{name}", організоване "{organizator}". Було подано "{num_appliaction}" заявок на загальну суму "{cost_money:.2f}" тис. гривень. Середня вартість проекту склала "{awerage:.2f}" гривень.'

print("\nФорматування за допомогою оператора %:")
print(text_percent)

print("\nФорматування за допомогою методу format():")
print(text_format)

print("\nФорматування за допомогою f-string:")
print(text_fstring)
