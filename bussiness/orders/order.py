
class Order(object):

    def __init__(self, name, phone, created, updated=None, email=None):
        self._name = name
        self._phone = phone
        self._email = email
        self._created = created
        self._updated = updated

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @property
    def email(self):
        return self._email

    @property
    def created(self):
        return self._created

    @property
    def updated(self):
        return self._updated

    def to_dict(self):
        return {
            'name': self.name, 'phone': self.phone, 'created': self.created, 'updated': self.updated,
            'email': self.email,
        }