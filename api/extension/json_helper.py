import datetime


def json_default(value):
    if isinstance(value, datetime.date):
        return f'{value.year}-{value.month}-{value.day}'
    else:
        return value.__dict__
