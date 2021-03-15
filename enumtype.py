# Code modified slightly from https://stackoverflow.com/a/38786737
from sqlalchemy.types import TypeDecorator, Integer

class EnumAsInteger(TypeDecorator):
    """Column type for storing Python enums in a database INTEGER column.

    This will behave erratically if a database value does not correspond to
    a known enum value.
    """
    impl = Integer # underlying database type

    def __init__(self, enum_type):
        super(EnumAsInteger, self).__init__()
        self.enum_type = enum_type

    def process_bind_param(self, value, dialect):
        if isinstance(value, self.enum_type):
            return value.value
        raise ValueError('expected %s value, got %s'
            % (self.enum_type.__name__, value.__class__.__name__))

    def process_result_value(self, value, dialect):
        return self.enum_type(value)

    def copy(self, **kwargs):
        return EnumAsInteger(self.enum_type)