from commons import call_api_asserts
from userede import *
from userede.mappers.receivables import Request
from userede.mappers.receivables import Response


def test_receivables(query_args, user, env):
    call_api_asserts(Receivables(user, env), Request(**query_args), Response)
