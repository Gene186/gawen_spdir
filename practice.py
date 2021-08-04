import requests

from common.yaml_util import read_yaml

# url = "https://demopmapi.liangyihui.net/official/login"
# json = {
#             "alipayId":"2088042142174230"
#             }
# # headers = {
# #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.8 Safari/537.36"
# # }
# res = requests.post(url=url,json=json)
# print(res)

# 111 TestApi.access_token = res.json()['access_token']
# 使用正则表达式提取
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
# 上传文件类型的post请求
# def  test_file_upload(self):
#     url = ""
#     value = {
#         "media":open(r"pwd","rb")
#     }
#     res = requests.post(url=url,files=value)

url = "https://demopmapi.liangyihui.net/official/patient/review"
access_token=read_yaml("access_token")
print(access_token)
data = {
            "pageSize": 10,
            "direction": 0,
            "reviewDt": ""
            }
header = {
"access_token":read_yaml("access_token")
}
res = requests.post(url=url,data=data,headers=header)
print(res.json())