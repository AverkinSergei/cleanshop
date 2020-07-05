
class Customer(object):
    """ Customer class. """

    def __init__(self, customer_id, name, phone, email):
        self._id = customer_id
        self._name = name
        self._phone = phone
        self._email = email

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @property
    def email(self):
        return self._email

    def to_dict(self):
        return {
            'id': self.id, 'name': self.name, 'phone': self.phone, 'email': self.email,
        }