import pytest



class TestMashang:
    # def setup(self):
    #     print("执行每条用例之前")
    #
    # def teardown(self):
    #     print("zhixing meitiaozhihou ")
    #
    # def setup_class(self):
    #     print('执行每个类之前')
    #
    # @pytest.mark.users
    #函数的前后置
    def test_baili(self,execute_database_sql):
        print('百里')
    #
    # @pytest.mark.smoke
    # def test_genge(self):
    #     print('根哥真帅')
    #
    # @pytest.mark.run(order=1)
    # def test_manman(self):
    #     print('媳妇最好看')
#类的前后置
@pytest.mark.usefixtures('execute_database_sql')
class TestAaa:

    def test_aaa(self):
        print("陈根好帅")

#会话的前后置
