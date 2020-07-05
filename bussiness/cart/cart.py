
class Cart(object):
    """ Cart object. """

    def __init__(self, cart_id, customer, created):
        self._id = cart_id
        self._customer = customer
        self._created = created

    @property
    def id(self):
        return self._id

    @property
    def customer(self):
        return self._customer

    @property
    def created(self):
        return self._created

    def to_dict(self):
        return {
            'id': self.id, 'customer': self.customer, 'created': self.created,
        }
