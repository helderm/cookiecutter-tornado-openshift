import tornado.testing as tte

"""
test_{{ cookiecutter.app_name }}
----------------------------------
Tests for `{{ cookiecutter.app_name }}` module.
"""

class MyTestCase(tte.AsyncTestCase):
    @tte.gen_test
    def test_http_fetch(self):
        client = tte.AsyncHTTPClient(self.io_loop)
        response = yield client.fetch("http://www.tornadoweb.org")
        # Test contents of response
        self.assertIn(b"FriendFeed", response.body)