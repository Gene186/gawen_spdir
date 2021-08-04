import pytest


@pytest.fixture(scope="session",autouse=True)
def execute_database_sql():
    print("在所有请求之前执行一次")
    yield
    print("在所有请求之后执行一次")