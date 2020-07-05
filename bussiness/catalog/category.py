
class Category(object):
    """ Product category class. """

    def __init__(self, category_id, name, parent=None):
        self._id = category_id
        self._name = name
        self._parent = parent

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def parent(self):
        return self.parent

    def to_dict(self):
        return {
            'name': self.name, 'parent': self.parent.to_dict if self.parent.to_dict() is not None else None,
        }
