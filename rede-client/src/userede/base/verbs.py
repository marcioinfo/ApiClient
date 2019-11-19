import related
from userede.base.fetchers import PageFetcher, SequenceFetcher


def GET(url, request_mapper, response_mapper, paging=False, sequence_field=None):

    def wrapper(self, request: request_mapper):
        assert isinstance(request, request_mapper), f"Request param must be a instance of {request_mapper}."

        content = self.get(url, params=related.to_dict(request)).content
        return related.from_json(content, response_mapper) if content else response_mapper()

    def pages(self, request: request_mapper):
        assert isinstance(request, request_mapper), f"Request param must be a instance of {request_mapper}."
        return PageFetcher(self, wrapper, request)

    def sequences(self, request: request_mapper):
        assert isinstance(request, request_mapper), f"Request param must be a instance of {request_mapper}."
        return SequenceFetcher(pages(self, request), sequence_field)

    if paging:
        return (wrapper, pages) if sequence_field is None else (wrapper, pages, sequences)
    else:
        return wrapper



