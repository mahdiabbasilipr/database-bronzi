# class of product
class Product:
    # price of one kilo bronze in now
    price_of_bronze = 0

    def __init__(self, name, code, weight, hight, width, price):
        self.name = name
        self.code = code
        self.weight = weight
        self.hight = hight
        self.width = width
        self.real_price = price
        price_for_customer = price + ((price * 30) / 100)
        self.price_for_customer = price_for_customer

    # get price from price of one kilo bronze and the weight of product
    def get_price_weight(self):
        self.real_price = Product.price_of_bronze * self.weight
        price_for_customer = self.real_price + ((self.real_price * 30) / 100)
        self.price_for_customer = price_for_customer

    def get_dict_data(self):
        dict_data = {
            'name': self.name,
            'code': self.code,
            'weight': self.weight,
            'hight': self.hight,
            'width': self.width,
            'price': self.real_price,
            'price_for_customer': self.price_for_customer
        }
        return dict_data
