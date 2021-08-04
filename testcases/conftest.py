import pytest

from common.yaml_util import clear_yaml


@pytest.fixture(scope="session",autouse=True)
def execute_database_sql():
    clear_yaml()
    yield
    print("在所有请求之后执行一次")