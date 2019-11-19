import related

#from  commons import call_api_asserts
from tests.commons import call_api_asserts
#from response_mocks import SALES
from tests.response_mocks import SALES
from userede import *
from userede.mappers.sales import Request
from userede.mappers.sales import Response


def test_parser():
    resp = related.from_json(SALES, Response)
    assert hasattr(resp, 'cursor')
    assert hasattr(resp, 'content')


def test_sales(query_args, user, env):
    call_api_asserts(Sales(user, env), Request(**query_args), Response)
