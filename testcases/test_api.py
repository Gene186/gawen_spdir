import pytest
from pip._vendor import requests
import re

from common.yaml_util import write_yaml


class TestApi:
    #111  access_token = ""
    access_token = ""
    global_token= ""
    session = requests.session()#会话

    # 必须带请求头，需要正则表达式，处理cookie鉴权以及session鉴权
    def test_get_token(self):
        url = "https://demopmapi.liangyihui.net/official/patient/review"
        # params = {
        #     "a":"",
        #     "b":""
        # }
        #res =requests.get(url=url)旧的
        res = TestApi.session.request("get",url=url)
        extract_data = {"access_token":res.json()['access_token']}
        write_yaml(extract_data)
        #111 result_value =res.text
        print(res.text)
        #111 TestApi.access_token = res.json()['access_token']
        #使用正则表达式提取
        # value = re.search('name="csrf_token" value="(.*?)"',result_value)#根据索要的值 左右边界匹配
        # print(value.group(1))#可以填写1或0
        # TestApi.global_token = value.group(1)
    #
    # def test_login(self):
    #     url = ''
    #     data = {
    #
    #     }
    #     headers={}
    #上传文件类型的post请求
    # def  test_file_upload(self):
    #     url = ""
    #     value = {
    #         "media":open(r"pwd","rb")
    #     }
    #     res = requests.post(url=url,files=value)



if __name__ == '__main__':
    pytest.main(['-vs'])

