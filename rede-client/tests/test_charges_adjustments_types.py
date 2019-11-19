from userede import *
from userede.mappers.charges.adjustments_types import Request
from userede.mappers.charges.adjustments_types import Response


def test_charges_adjustments_types(query_args, user, env):
    charges = ChargesAdjustmentTypes(user, env)
    response = charges.query(Request())

    assert isinstance(response, Response)
