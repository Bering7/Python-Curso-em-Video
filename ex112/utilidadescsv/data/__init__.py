def readMoney(price):
    price = price.replace('R$', '').replace(',', '.').strip()
    return float(price)