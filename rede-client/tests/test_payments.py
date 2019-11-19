from commons import call_api_asserts
from userede import *
from userede.mappers.payments import Request
from userede.mappers.payments import Response


def test_payments(query_args, user, env):
    call_api_asserts(Payments(user, env), Request(**query_args), Response)
