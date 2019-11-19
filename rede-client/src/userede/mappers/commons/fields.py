from attr import NOTHING, attrib
from related import _init_fields
from decimal import Decimal


def DecimalField(default=NOTHING, required=True, repr=True, cmp=True,
                 key=None):
    """
    Custom decimal field on a model with a converter that preserve two decimal digits.
    :param default: any decimal value
    :param bool required: whether or not the object is invalid if not provided.
    :param bool repr: include this field should appear in object's repr.
    :param bool cmp: include this field in generated comparison.
    :param string key: override name of the value when converted to dict.
    """
    default = _init_fields.init_default(required, default, None)
    validator = _init_fields.init_validator(required, Decimal)
    return attrib(default=default, converter=lambda x: Decimal(str(x)),
                  validator=validator, repr=repr, cmp=cmp,
                  metadata=dict(key=key))