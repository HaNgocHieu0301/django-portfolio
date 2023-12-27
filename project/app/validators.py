from django.core.exceptions import ValidationError


def validate_phone(value):
    if len(value) < 10:
        raise ValidationError('Phone needs to be of length 10 characters')
