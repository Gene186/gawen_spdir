import pytest
from pip._vendor import requests
import re

from common.yaml_util import write_yaml, read_yaml, read_testcase_yaml
from common.all_request import AllRequest

class TestApi:
    #111  access_token = ""
    # global_token= ""
    session = requests.session()    #会话

    @pytest.mark.parametrize("caseinfo",read_testcase_yaml("get_token.yml"))
    def test01_caseinfo(self,caseinfo):
        print(caseinfo)
        url = caseinfo['request']['url']
        method = caseinfo['request']['method']
        params = caseinfo['request']['params']

        res=AllRequest().send_all_request(method,url=url,data=params)
        # res =TestApi.session.request(method,url=url,params=params)
        extract_data = {"access_token":res.json()['access_token']}
        write_yaml(extract_data)
        print(res.text)