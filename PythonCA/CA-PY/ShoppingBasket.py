from fileImport import fetch_content


class ShoppingBasket:

    def __init__(self):
        self.__basket_dict = dict()

    priceList = fetch_content('cartItems')
    # print(priceList)

    def add_to_cart(self, item, qty):
        if item not in ShoppingBasket.priceList:
            raise ValueError("Please review cart Item Error")
        if qty <= 0:
            raise ValueError("Minimum Quantity Exception")
        self.__basket_dict[item] = qty + self.__basket_dict.get(item, 0)

    def order(self):
        total = 0
        for item_val, item_count in self.__basket_dict.items():
            total += item_count * ShoppingBasket.priceList.get(item_val)
        return total
