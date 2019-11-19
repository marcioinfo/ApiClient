import related
from inspect import getmembers, signature


@related.immutable
class Cursor:
    hasNextKey = related.BooleanField()
    nextKey = related.StringField(required=False)


@related.immutable
class ResponsePage:
    cursor = related.ChildField(Cursor)


@related.immutable
class RequestPage:
    size = related.IntegerField(required=False)
    pageKey = related.StringField(required=False)

    def next_request(self, pageKey):
        kwargs = {name: value for name, value in getmembers(self) if name in signature(self.__class__).parameters.keys()}
        kwargs.update({'pageKey': pageKey})
        return self.__class__(**kwargs)

