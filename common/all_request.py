import json
import requests

class AllRequest:

    session = requests.session()

    def send_all_request(self,method,url,data,**kwargs):

        method =  str(method).lower()
        res = None
        if method == 'get':
            res= AllRequest.session.request(method=method,url=url,params=data,**kwargs)

        elif method == 'post':
            strdata = json.dumps(data)#转换成字符串格式
            res=AllRequest.session.request(method=method,url=url,data=strdata,**kwargs)

        elif method == 'put':
            strdata = json.dumps(data)
            res=AllRequest.session.request(method=method, url=url, data=strdata,**kwargs)
        else:
            print("不支持该请求方式")
        return res

