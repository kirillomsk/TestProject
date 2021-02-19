from requests import get, post
from conftest import url


class Test_API_post:
    def setup_method(self):
        global response
        response = post(url)

    def test_post_status(self):
        assert response.status_code == 201

    def test_post_not_none(self):
        assert response.json() is not None

    def test_post_data(self):
        assert 'id' in response.json(), response.json()

    def test_post_data_id(self):
        assert response.json()['id'] is not None


class Test_API_get:
    def setup_method(self):
        global response
        response = get(url)

    def test_get_ststus(self):
        assert response.status_code == 200

    def test_get_all_data(self):
        assert len(response.json()) == 100

    def test_get_data_four_line(self):
        for i in range(100):
            assert len(response.json()[i]) == 4

    def test_get_data_userid(self):
        for i in range(100):
            assert 'userId' in response.json()[i]

    def test_get_data_id(self):
        for i in range(100):
            assert 'id' in response.json()[i]

    def test_get_data_title(self):
        for i in range(100):
            assert 'title' in response.json()[i]

    def test_get_data_body(self):
        for i in range(100):
            assert 'body' in response.json()[i]

    def test_get_data_userid_not_none(self):
        for i in range(100):
            assert response.json()[i]['userId'] is not None

    def test_get_data_id_not_none(self):
        for i in range(100):
            assert response.json()[i]['id'] is not None

    def test_get_data_title_not_none(self):
        for i in range(100):
            assert response.json()[i]['title'] is not None

    def test_get_data_body_not_none(self):
        for i in range(100):
            assert response.json()[i]['body'] is not None
