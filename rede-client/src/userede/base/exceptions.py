import related


@related.immutable
class RequestGetError(Exception):
    status_code = related.IntegerField()
    message = related.StringField()
