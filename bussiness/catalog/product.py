
class Product(object):
    """ Product class """

    def __init__(self, name, price, description, published):
        self._name = name
        self._price = price
        self._description = description
        self._published = published

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def description(self):
        return self._description

    @property
    def published(self):
        return self.published

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'description': self.description,
            'published': self.published,
        }
