from pages.triangle_page import TrianglePage
import pytest

link = "https://playground.learnqa.ru/puzzle/triangle"

@pytest.fixture(scope="session")
def page(browser):
    page = TrianglePage(browser, link)
    page.open()
    yield page

class TestTianglePage():
    

    @pytest.mark.parametrize("a, b, c", 
                             [
                                 (3, 4, 5), (4, 5, 6), (2, 3, 4), 
                                 (4, 4, 4), (5, 4, 4), (3.4, 4.1, 4.9)
                                 ])
    def test_should_be_pass_positive_tests(self, a, b, c, page):
        msg = page.check_triangle(a,b,c)
        assert page.is_info_message_error(msg) == False, msg.text[0:msg.text.find('.')]
    
    @pytest.mark.parametrize("a, b, c", 
                             [
                                 (0,0,0), ("a", 5, 6), (2, "b", 4), 
                                 (4, 4, "c"), ("a", "b", "c"),
                                 (3000000000, 3000000000, 3000000000), ('','',''),
                                 ("SELECT * FROM users", 1, 2),
                                 ("<Script>alert('Hacked?')</Script>", 3, 4)])
    def test_should_not_be_pass_negative_tests(self, a, b, c, page):
        msg = page.check_triangle(a,b,c)
        assert page.is_info_message_error(msg) == True, msg.text[0:msg.text.find('.')]
    

