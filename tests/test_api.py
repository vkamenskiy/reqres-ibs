import requests


class TestGetListUsers:
    def test_list_users_response_successful(self):
        response = requests.get("https://reqres.in/api/users?page=2")

        assert response.status_code == 200
        assert response.json() == {
            "page": 2,
            "per_page": 6,
            "total": 12,
            "total_pages": 2,
            "data": [
                {
                    "id": 7,
                    "email": "michael.lawson@reqres.in",
                    "first_name": "Michael",
                    "last_name": "Lawson",
                    "avatar": "https://reqres.in/img/faces/7-image.jpg",
                },
                {
                    "id": 8,
                    "email": "lindsay.ferguson@reqres.in",
                    "first_name": "Lindsay",
                    "last_name": "Ferguson",
                    "avatar": "https://reqres.in/img/faces/8-image.jpg",
                },
                {
                    "id": 9,
                    "email": "tobias.funke@reqres.in",
                    "first_name": "Tobias",
                    "last_name": "Funke",
                    "avatar": "https://reqres.in/img/faces/9-image.jpg",
                },
                {
                    "id": 10,
                    "email": "byron.fields@reqres.in",
                    "first_name": "Byron",
                    "last_name": "Fields",
                    "avatar": "https://reqres.in/img/faces/10-image.jpg",
                },
                {
                    "id": 11,
                    "email": "george.edwards@reqres.in",
                    "first_name": "George",
                    "last_name": "Edwards",
                    "avatar": "https://reqres.in/img/faces/11-image.jpg",
                },
                {
                    "id": 12,
                    "email": "rachel.howell@reqres.in",
                    "first_name": "Rachel",
                    "last_name": "Howell",
                    "avatar": "https://reqres.in/img/faces/12-image.jpg",
                },
            ],
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!",
            },
        }

    def test_another_list_users_response_successful(self):
        response = requests.get("https://reqres.in/api/users?page=1")

        assert response.status_code == 200
        assert response.json() == {
            "page": 1,
            "per_page": 6,
            "total": 12,
            "total_pages": 2,
            "data": [
                {
                    "id": 1,
                    "email": "george.bluth@reqres.in",
                    "first_name": "George",
                    "last_name": "Bluth",
                    "avatar": "https://reqres.in/img/faces/1-image.jpg",
                },
                {
                    "id": 2,
                    "email": "janet.weaver@reqres.in",
                    "first_name": "Janet",
                    "last_name": "Weaver",
                    "avatar": "https://reqres.in/img/faces/2-image.jpg",
                },
                {
                    "id": 3,
                    "email": "emma.wong@reqres.in",
                    "first_name": "Emma",
                    "last_name": "Wong",
                    "avatar": "https://reqres.in/img/faces/3-image.jpg",
                },
                {
                    "id": 4,
                    "email": "eve.holt@reqres.in",
                    "first_name": "Eve",
                    "last_name": "Holt",
                    "avatar": "https://reqres.in/img/faces/4-image.jpg",
                },
                {
                    "id": 5,
                    "email": "charles.morris@reqres.in",
                    "first_name": "Charles",
                    "last_name": "Morris",
                    "avatar": "https://reqres.in/img/faces/5-image.jpg",
                },
                {
                    "id": 6,
                    "email": "tracey.ramos@reqres.in",
                    "first_name": "Tracey",
                    "last_name": "Ramos",
                    "avatar": "https://reqres.in/img/faces/6-image.jpg",
                },
            ],
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!",
            },
        }

    def test_list_users_with_empty_data(self):
        response = requests.get("https://reqres.in/api/users?page=3")

        assert response.status_code == 200
        assert response.json() == {
            "page": 3,
            "per_page": 6,
            "total": 12,
            "total_pages": 2,
            "data": [],
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!",
            },
        }

    def test_request_without_page_number(self):
        response = requests.get("https://reqres.in/api/users?page=")

        assert response.status_code == 200
        assert response.json() == {
            "page": 1,
            "per_page": 6,
            "total": 12,
            "total_pages": 2,
            "data": [
                {
                    "id": 1,
                    "email": "george.bluth@reqres.in",
                    "first_name": "George",
                    "last_name": "Bluth",
                    "avatar": "https://reqres.in/img/faces/1-image.jpg",
                },
                {
                    "id": 2,
                    "email": "janet.weaver@reqres.in",
                    "first_name": "Janet",
                    "last_name": "Weaver",
                    "avatar": "https://reqres.in/img/faces/2-image.jpg",
                },
                {
                    "id": 3,
                    "email": "emma.wong@reqres.in",
                    "first_name": "Emma",
                    "last_name": "Wong",
                    "avatar": "https://reqres.in/img/faces/3-image.jpg",
                },
                {
                    "id": 4,
                    "email": "eve.holt@reqres.in",
                    "first_name": "Eve",
                    "last_name": "Holt",
                    "avatar": "https://reqres.in/img/faces/4-image.jpg",
                },
                {
                    "id": 5,
                    "email": "charles.morris@reqres.in",
                    "first_name": "Charles",
                    "last_name": "Morris",
                    "avatar": "https://reqres.in/img/faces/5-image.jpg",
                },
                {
                    "id": 6,
                    "email": "tracey.ramos@reqres.in",
                    "first_name": "Tracey",
                    "last_name": "Ramos",
                    "avatar": "https://reqres.in/img/faces/6-image.jpg",
                },
            ],
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!",
            },
        }


class TestGetSingleUser:
    def test_single_user_response_successful(self):
        response = requests.get("https://reqres.in/api/users/2")

        assert response.status_code == 200
        assert response.json() == {
            "data": {
                "id": 2,
                "email": "janet.weaver@reqres.in",
                "first_name": "Janet",
                "last_name": "Weaver",
                "avatar": "https://reqres.in/img/faces/2-image.jpg",
            },
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!",
            },
        }

    def test_another_single_user_response_successful(self):
        response = requests.get("https://reqres.in/api/users/3")

        assert response.status_code == 200
        assert response.json() == {
            "data": {
                "id": 3,
                "email": "emma.wong@reqres.in",
                "first_name": "Emma",
                "last_name": "Wong",
                "avatar": "https://reqres.in/img/faces/3-image.jpg",
            },
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!",
            },
        }

    def test_single_user_not_found(self):
        response = requests.get("https://reqres.in/api/users/23")

        assert response.status_code == 404
        assert response.json() == {}


class TestPostCreate:
    def test_create_user_with_name_and_job(self):
        response = requests.post(
            "https://reqres.in/api/users", {"name": "morpheus", "job": "leader"}
        )
        name = response.json()["name"]
        job = response.json()["job"]

        assert name == "morpheus"
        assert job == "leader"
        assert response.status_code == 201

    def test_create_user_with_name(self):
        response = requests.post(
            "https://reqres.in/api/users", {"name": "morpheus"}
        )
        name = response.json()["name"]

        assert name == "morpheus"
        assert response.status_code == 201

    def test_create_user_with_job(self):
        response = requests.post(
            "https://reqres.in/api/users", {"job": "leader"}
        )
        job = response.json()["job"]

        assert job == "leader"
        assert response.status_code == 201

    def test_create_user_with_empty_data(self):
        response = requests.post(
            "https://reqres.in/api/users"
        )

        assert response.status_code == 201


class TestPutUpdate:
    def test_update_only_job(self):
        response = requests.put(
            "https://reqres.in/api/users/9", {"job": "zion resident"}
        )
        job = response.json()["job"]

        assert job == "zion resident"
        assert response.status_code == 200

    def test_update_only_name(self):
        response = requests.put(
            "https://reqres.in/api/users/9", {"name": "morpheus"}
        )
        name = response.json()["name"]

        assert name == "morpheus"
        assert response.status_code == 200

    def test_update_name_and_job(self):
        response = requests.put(
            "https://reqres.in/api/users/9", {"name": "neo", "job": "hero"}
        )
        name = response.json()["name"]
        job = response.json()["job"]

        assert name == "neo"
        assert job == "hero"
        assert response.status_code == 200


class TestPatchUpdate:
    def test_update_only_job(self):
        response = requests.patch(
            "https://reqres.in/api/users/9", {"job": "zion resident"}
        )
        job = response.json()["job"]

        assert job == "zion resident"
        assert response.status_code == 200

    def test_update_only_name(self):
        response = requests.patch(
            "https://reqres.in/api/users/9", {"name": "morpheus"}
        )
        name = response.json()["name"]

        assert name == "morpheus"
        assert response.status_code == 200

    def test_update_name_and_job(self):
        response = requests.patch(
            "https://reqres.in/api/users/9", {"name": "neo", "job": "hero"}
        )
        name = response.json()["name"]
        job = response.json()["job"]

        assert name == "neo"
        assert job == "hero"
        assert response.status_code == 200


class TestDeleteDelete:
    def test_delete_user(self):
        response = requests.delete("https://reqres.in/api/users/2")

        assert response.status_code == 204
        assert len(response.content) == 0


class TestPostRegister:
    def test_register_successful(self):
        response = requests.post(
            "https://reqres.in/api/register",
            {"email": "eve.holt@reqres.in", "password": "pistol"},
        )
        user_id = response.json()["id"]
        result = requests.get(f"https://reqres.in/api/users/{user_id}")
        email = result.json()["data"]["email"]

        assert response.status_code == 200
        assert result.status_code == 200
        assert email == "eve.holt@reqres.in"
        assert response.json() == {"id": 4, "token": "QpwL5tke4Pnpja7X4"}

    def test_register_without_password(self):
        response = requests.post("https://reqres.in/api/register", {"email": "sydney@fife"})

        assert response.status_code == 400
        assert response.json() == {"error": "Missing password"}

    def test_register_without_email(self):
        response = requests.post("https://reqres.in/api/register", {"password": "pistol"})

        assert response.status_code == 400
        assert response.json() == {"error": "Missing email or username"}


class TestPostLogin:
    def test_login_successful(self):
        response = requests.post(
            "https://reqres.in/api/login",
            {"email": "eve.holt@reqres.in", "password": "cityslicka"},
        )

        assert response.status_code == 200
        assert response.json() == {"token": "QpwL5tke4Pnpja7X4"}

    def test_login_without_password(self):
        response = requests.post("https://reqres.in/api/login", {"email": "peter@klaven"})

        assert response.status_code == 400
        assert response.json() == {"error": "Missing password"}

    def test_login_without_email(self):
        response = requests.post("https://reqres.in/api/login", {"password": "cityslicka"})

        assert response.status_code == 400
        assert response.json() == {"error": "Missing email or username"}


class TestGetDelayedResponse:
    def test_delayed_response_successful(self):
        response = requests.get("https://reqres.in/api/users?delay=3")

        assert response.status_code == 200
        assert response.json() == {
            "page": 1,
            "per_page": 6,
            "total": 12,
            "total_pages": 2,
            "data": [
                {
                    "id": 1,
                    "email": "george.bluth@reqres.in",
                    "first_name": "George",
                    "last_name": "Bluth",
                    "avatar": "https://reqres.in/img/faces/1-image.jpg",
                },
                {
                    "id": 2,
                    "email": "janet.weaver@reqres.in",
                    "first_name": "Janet",
                    "last_name": "Weaver",
                    "avatar": "https://reqres.in/img/faces/2-image.jpg",
                },
                {
                    "id": 3,
                    "email": "emma.wong@reqres.in",
                    "first_name": "Emma",
                    "last_name": "Wong",
                    "avatar": "https://reqres.in/img/faces/3-image.jpg",
                },
                {
                    "id": 4,
                    "email": "eve.holt@reqres.in",
                    "first_name": "Eve",
                    "last_name": "Holt",
                    "avatar": "https://reqres.in/img/faces/4-image.jpg",
                },
                {
                    "id": 5,
                    "email": "charles.morris@reqres.in",
                    "first_name": "Charles",
                    "last_name": "Morris",
                    "avatar": "https://reqres.in/img/faces/5-image.jpg",
                },
                {
                    "id": 6,
                    "email": "tracey.ramos@reqres.in",
                    "first_name": "Tracey",
                    "last_name": "Ramos",
                    "avatar": "https://reqres.in/img/faces/6-image.jpg",
                },
            ],
            "support": {
                "url": "https://reqres.in/#support-heading",
                "text": "To keep ReqRes free, contributions towards server costs are appreciated!",
            },
        }
