from inspect import isgenerator


def call_api_asserts(endpoint, request, response_mapper):
    assert isinstance(endpoint.query(request), response_mapper)
    assert isgenerator(endpoint.pages(request).iterable())
