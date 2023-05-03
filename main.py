from currency_converter import CurrencyConverter

c = CurrencyConverter()
print("Список доступных валют:\nUSD - доллары(США)\nEUR - евро(Европа)\nHRK - куны(Хорватия)\nPLN - злотый(Польша)\nBRL - реал(Бразилия)\nEEK - крона(Эстония)\nDKK - крона(Дания)\nRON - лей(Румыния)\nLVL - лат(Латвия)\nNOK - крона(Норвегия)\nHUF - форинт(Венгрия)\nLTL - лит(Литва)\nHKD - доллар(Гонконг)\nKRW - вона(Южная Корея)\nMYR - ринггит(Малазия)\nJPY - иена(Япония)")

first = input("какую валюту конвертируешь\n")
num = int(input('количество валюты для конвертации\n'))
second = input('во что конвертируешь\n')
print(c.convert(num, first, second))