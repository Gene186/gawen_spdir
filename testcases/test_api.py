import pytest
from pip._vendor import requests
import re

from common.yaml_util import write_yaml, read_yaml


class TestApi:
    #111  access_token = ""
    global_token= ""
    session = requests.session()#会话

    # 必须带请求头，需要正则表达式，处理cookie鉴权以及session鉴权
    def test_get_token(self):
        url = "https://demopmapi.liangyihui.net/official/login"
        data = {
            "alipayId":"2088042142174230"
            }
        res = TestApi.session.request("post",url=url,json=data)
        extract_data = {"access_token":res.json()['data']}
        write_yaml(extract_data)
        #111 result_value =res.text
        print(res.text)

    def test_search_review(self):
        url = "https://demopmapi.liangyihui.net/official/patient/review"
        data = {
            "pageSize": 10,
            "direction": 0,
            "reviewDt": "",
            "access_token":read_yaml("access_token")
        }
        # header = {
        #     "access_token":read_yaml("access_token")
        # }
        res = TestApi.session.request("post",url=url,data=data)
        print(res.json())






if __name__ == '__main__':
    pytest.main(['-vs'])

