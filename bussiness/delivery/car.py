
class Car(object):
    """ Delivery car class. """

    def __init__(self, car_id, number, name):
        self._id = car_id
        self._number = number
        self._name = name

    @property
    def id(self):
        return self._id

    @property
    def number(self):
        return self._number

    @property
    def name(self):
        return self._name

    def to_dict(self):
        return {
            'id': self.id, 'number': self.number, 'name': self.name,
        }
