from userede import *
from userede.mappers.charges.summary import Request
from userede.mappers.charges.summary import Response


def test_charges_summary(query_args, user, env):
    charges = ChargesSummary(user, env)
    response = charges.query(Request(**query_args))

    assert isinstance(response, Response)

