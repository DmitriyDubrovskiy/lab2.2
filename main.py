class Converter:
    def __init__(self, usd, eur, pln):
        self.usd = usd
        self.eur = eur
        self.pln = pln

    def convert_to_uah(self, amount, currency):
        if currency == "USD":
            return amount * self.usd
        elif currency == "EUR":
            return amount * self.eur
        elif currency == "PLN":
            return amount * self.pln
        else:
            return "Invalid currency"

    def convert_from_uah(self, amount, currency):
        if currency == "USD":
            return amount / self.usd
        elif currency == "EUR":
            return amount / self.eur
        elif currency == "PLN":
            return amount / self.pln
        else:
            return "Invalid currency"

# Приклад використання класу Converter
usd_rate = 28.5
eur_rate = 33.2
pln_rate = 7.5

converter = Converter(usd_rate, eur_rate, pln_rate)

# Конвертація з гривні в іншу валюту
amount_in_uah = 1000
converted_amount_usd = converter.convert_to_uah(amount_in_uah, "USD")
print(f"{amount_in_uah} UAH is approximately {converted_amount_usd:.2f} USD")

# Конвертація з іншої валюти в гривню
amount_in_eur = 50
converted_amount_uah = converter.convert_from_uah(amount_in_eur, "EUR")
print(f"{amount_in_eur} EUR is approximately {converted_amount_uah:.2f} UAH")
