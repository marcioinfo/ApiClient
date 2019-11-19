import related


class Response:
    code = related.IntegerField()
    description = related.StringField()