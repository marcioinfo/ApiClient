from userede.mappers.commons.paging import ResponsePage
from typing import Callable, Iterable


class PageFetcher:
    def __init__(self, obj, resource: Callable[[], ResponsePage], request):
        self.resource = resource
        self.request = request
        self.obj = obj

    def iterable(self) -> Iterable:
        response = self.resource(self.obj, self.request)
        yield response.content
        while response.cursor.hasNextKey:
            request = self.request.next_request(response.cursor.nextKey)
            response = self.resource(self.obj, request)
            yield response.content

    def all(self):
        return [page for page in self.iterable()]


class SequenceFetcher:
    def __init__(self, page_fetcher: PageFetcher, sequence_field):
        self.page_fetcher = page_fetcher
        self.sequence_field = sequence_field

    def iterable(self) -> Iterable:
        for page in self.page_fetcher.iterable():
            for row in getattr(page, self.sequence_field):
                yield row

    def all(self):
        return [row for row in self.iterable()]
