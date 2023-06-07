import json

import requests
from selene import have
from selene.support.shared import browser


class TestMainRequests:
    def test_get_list_users(self):
        json_response = {
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
        response_status_code = 200

        browser.open("")
        browser.element(".response-code").should(have.text(f"{response_status_code}"))
        browser.element('[data-key="output-response"]').should(
            have.text(json.dumps(obj=json_response, indent=4))
        )

        response = requests.get("https://reqres.in/api/users?page=2")

        assert response.status_code == response_status_code
        assert response.json() == json_response

    def test_get_single_user(self):
        json_response = {
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
        response_status_code = 200

        browser.open("")
        browser.element("[data-id=users-single]").click()
        browser.element(".response-code").should(have.text(f"{response_status_code}"))
        browser.element('[data-key="output-response"]').should(
            have.text(
                json.dumps(
                    obj=json_response,
                    indent=4,
                )
            )
        )

        response = requests.get("https://reqres.in/api/users/2")

        assert response.status_code == response_status_code
        assert response.json() == json_response

    def test_get_single_user_not_found(self):
        json_response = {}
        response_status_code = 404

        browser.open("")
        browser.element("[data-id=users-single-not-found]").click()
        browser.element(".response-code").should(have.text(f"{response_status_code}"))
        browser.element('[data-key="output-response"]').should(
            have.text(json.dumps(obj=json_response))
        )

        response = requests.get("https://reqres.in/api/users/23")

        assert response.status_code == response_status_code
        assert response.json() == json_response

    def test_post_create(self):
        text_in_json_response = '"name": "morpheus",\n    "job": "leader"'
        response_status_code = 201

        browser.open("")
        browser.element("[data-id=post]").click()
        browser.element(".response-code").should(have.text(f"{response_status_code}"))
        browser.element('[data-key="output-response"]').should(
            have.text(text_in_json_response)
        )

        response = requests.post(
            "https://reqres.in/api/users", {"name": "morpheus", "job": "leader"}
        )
        name = response.json()["name"]
        job = response.json()["job"]

        assert name in text_in_json_response
        assert job in text_in_json_response
        assert response.status_code == response_status_code

    def test_put_update(self):
        text_in_json_response = '"name": "morpheus",\n    "job": "zion resident"'
        response_status_code = 200

        browser.open("")
        browser.element("[data-id=put]").click()
        browser.element(".response-code").should(have.text(f"{response_status_code}"))
        browser.element('[data-key="output-response"]').should(
            have.text(text_in_json_response)
        )

        response = requests.put(
            "https://reqres.in/api/users/2",
            {"name": "morpheus", "job": "zion resident"},
        )
        name = response.json()["name"]
        job = response.json()["job"]

        assert name in text_in_json_response
        assert job in text_in_json_response
        assert response.status_code == response_status_code

    def test_patch_update(self):
        text_in_json_response = '"name": "morpheus",\n    "job": "zion resident"'
        response_status_code = 200

        browser.open("")
        browser.element("[data-id=patch]").click()
        browser.element(".response-code").should(have.text(f"{response_status_code}"))
        browser.element('[data-key="output-response"]').should(
            have.text(text_in_json_response)
        )

        response = requests.patch(
            "https://reqres.in/api/users/2",
            {"name": "morpheus", "job": "zion resident"},
        )
        name = response.json()["name"]
        job = response.json()["job"]

        assert name in text_in_json_response
        assert job in text_in_json_response
        assert response.status_code == response_status_code

    def test_delete(self):
        json_response = ""
        response_status_code = 204

        browser.open("")
        browser.element("[data-id=delete]").click()
        browser.element(".response-code").should(have.text(f"{response_status_code}"))
        browser.element('[data-key="output-response"]').should(have.text(json_response))

        response = requests.delete("https://reqres.in/api/users/2")

        assert response.status_code == response_status_code
        assert len(response.content) == len(json_response)

    def test_post_register_successful(self):
        json_response = {"id": 4, "token": "QpwL5tke4Pnpja7X4"}
        response_status_code = 200

        browser.open("")
        browser.element("[data-id=register-successful]").click()
        browser.element(".response-code").should(have.text(f"{response_status_code}"))
        browser.element('[data-key="output-response"]').should(
            have.text(json.dumps(obj=json_response, indent=4))
        )

        response = requests.post(
            "https://reqres.in/api/register",
            {"email": "eve.holt@reqres.in", "password": "pistol"},
        )

        assert response.status_code == response_status_code
        assert response.json() == json_response

    def test_post_register_unsuccessful(self):
        json_response = {"error": "Missing password"}
        response_status_code = 400

        browser.open("")
        browser.element("[data-id=register-unsuccessful]").click()
        browser.element(".response-code").should(have.text(f"{response_status_code}"))
        browser.element('[data-key="output-response"]').should(
            have.text(json.dumps(obj=json_response, indent=4))
        )

        response = requests.post(
            "https://reqres.in/api/register", {"email": "sydney@fife"}
        )

        assert response.status_code == response_status_code
        assert response.json() == json_response

    def test_post_login_successful(self):
        json_response = {"token": "QpwL5tke4Pnpja7X4"}
        response_status_code = 200

        browser.open("")
        browser.element("[data-id=login-successful]").click()
        browser.element(".response-code").should(have.text(f"{response_status_code}"))
        browser.element('[data-key="output-response"]').should(
            have.text(json.dumps(obj=json_response, indent=4))
        )

        response = requests.post(
            "https://reqres.in/api/login",
            {"email": "eve.holt@reqres.in", "password": "cityslicka"},
        )

        assert response.status_code == response_status_code
        assert response.json() == json_response

    def test_post_login_unsuccessful(self):
        json_response = {"error": "Missing password"}
        response_status_code = 400

        browser.open("")
        browser.element("[data-id=login-unsuccessful]").click()
        browser.element(".response-code").should(have.text(f"{response_status_code}"))
        browser.element('[data-key="output-response"]').should(
            have.text(json.dumps(obj=json_response, indent=4))
        )

        response = requests.post(
            "https://reqres.in/api/login", {"email": "peter@klaven"}
        )

        assert response.status_code == response_status_code
        assert response.json() == json_response

    def test_get_delayed_response(self):
        json_response = {
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
        response_status_code = 200

        browser.open("")
        browser.element("[data-id=delay]").click()
        browser.element(".response-code").should(have.text(f"{response_status_code}"))
        browser.element('[data-key="output-response"]').should(
            have.text(
                json.dumps(
                    obj=json_response,
                    indent=4,
                )
            )
        )

        response = requests.get("https://reqres.in/api/users?delay=3")

        assert response.status_code == response_status_code
        assert response.json() == json_response