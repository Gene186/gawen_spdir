import yaml
import os



#读取yaml文件
def  read_yaml(key):
    with open(os.getcwd()+'/1extract1.yaml',encoding='utf-8') as f:#打开yaml文件
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value[key]

#写入yaml文件,mode='a'表示追加的方式写入
def  write_yaml(data):
    with open(os.getcwd()+'/extract11.yaml',encoding='utf-8',mode="a") as f:
        yaml.dump(data,stream=f,allow_unicode=True)

#清空yaml文件
def clear_yaml():
    with open(os.getcwd() + '/1extract1.yaml', encoding='utf-8', mode="w") as f:
        f.truncate()

#读取yaml文件
def  read_testcase_yaml(yaml_name):
    with open(os.getcwd()+'/testcases'+yaml_name,encoding='utf-8') as f:#打开yaml文件
        value = yaml.load(stream=f,Loader=yaml.FullLoader)
        return value[yaml_name]