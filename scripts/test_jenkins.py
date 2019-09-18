import allure


class TestJen:

    @allure.step("测试步骤")
    def test_jen(self):
        allure.attach("名称", "内容")
        assert True
