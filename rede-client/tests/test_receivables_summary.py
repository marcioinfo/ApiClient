from commons import call_api_asserts
from userede import *
from userede.mappers.receivables.summary import Request
from userede.mappers.receivables.summary import Response


def test_receivables_summary(query_args, user, env):
    call_api_asserts(ReceivablesSummary(user, env), Request(**query_args), Response)
