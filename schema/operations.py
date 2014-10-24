READ = 0
CREATE = 1
UPDATE = 2
DELETE = 3
FIND_UNIQUE = 4
FIND_PRIMARY = 5
FIND_ONE_PRIMARY = 6


class Base():
    def __init__(self, values):
        self.values = values


class Equal(Base):
    pass


class GreaterThan(Base):
    pass


class SmallerThan(Base):
    pass


class Contains(Base):
    pass


class Exclude(Base):
    pass
