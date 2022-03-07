# Read CartItems & Price List using split func.

with open('cartItems', 'w') as f:
    f.write("""bread 1.49
milk 0.99
cheese 2.99""")


def fetch_content(filename):
    contents = {line.split()[0]: float(line.split()[1]) for line in open(filename)}
    return contents


priceList = fetch_content('cartItems')
print(priceList)
