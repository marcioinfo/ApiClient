from commons import call_api_asserts
from userede import *
from userede.mappers.sales.installments import Request
from userede.mappers.sales.installments import Response


def test_sales_installments(query_args, user, env):
    call_api_asserts(SalesInstallments(user, env), Request(**query_args), Response)
