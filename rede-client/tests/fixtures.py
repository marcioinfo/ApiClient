from datetime import date

import pytest

from userede import *


@pytest.fixture(scope="module")
def query_args():
    return {"parentCompanyNumber": 77879899,
            "subsidiaries": 77879899,
            "startDate": date(2019, 7, 1),
            "endDate": date(2019, 7, 31)}


@pytest.fixture(scope="module")
def user():
    return DEFAULT_USER


@pytest.fixture(scope="module")
def env():
    return PRODUCTION