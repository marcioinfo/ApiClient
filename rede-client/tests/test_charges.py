from commons import call_api_asserts
from userede import *
from userede.mappers.charges import Request
from userede.mappers.charges import Response


def test_charges(query_args, user, env):
    call_api_asserts(Charges(user, env), Request(**query_args), Response)
