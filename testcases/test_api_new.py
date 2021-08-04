import pytest
from pip._vendor import requests
import re

from common.yaml_util import write_yaml, read_yaml


class TestApi:
    #111  access_token = ""
    # global_token= ""
    session = requests.session()    #会话

    @pytest.mark.parametrize("name,age",[['根哥','13'],['百里','6']])
    def test01_caseinfo(self,name,age):
        print(name,age)