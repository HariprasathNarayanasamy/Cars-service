# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.login_details import LoginDetails  # noqa: E501
from swagger_server.models.login_info import LoginInfo  # noqa: E501
from swagger_server.models.model200_update_user_response import Model200UpdateUserResponse  # noqa: E501
from swagger_server.models.model200_user_deleted_response import Model200UserDeletedResponse  # noqa: E501
from swagger_server.models.model200_user_details_response import Model200UserDetailsResponse  # noqa: E501
from swagger_server.models.model201_user_created_response import Model201UserCreatedResponse  # noqa: E501
from swagger_server.models.model400_bad_request_response import Model400BadRequestResponse  # noqa: E501
from swagger_server.models.model401_unauthorized_response import Model401UnauthorizedResponse  # noqa: E501
from swagger_server.models.model403_forbidden_response import Model403ForbiddenResponse  # noqa: E501
from swagger_server.models.model404_not_found_response import Model404NotFoundResponse  # noqa: E501
from swagger_server.models.model503_server_unavailable_response import Model503ServerUnavailableResponse  # noqa: E501
from swagger_server.models.token_info import TokenInfo  # noqa: E501
from swagger_server.models.update_user_info import UpdateUserInfo  # noqa: E501
from swagger_server.models.user_details import UserDetails  # noqa: E501
from swagger_server.models.user_info import UserInfo  # noqa: E501
from swagger_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_add_user_alreadyexisting_return400(self):
        """Test case for add_user

        
        """
        body = {
            "user_name": "user6",
            "first_name": "user6",
            "last_name": "user6",
            "email": "user6@user.com",
            "phone": "9876543210",
            "password": "user6"
            }
        response = self.client.open(
            '/userservice/v1/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert403(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    def test_add_user_return200(self):
        """Test case for add_user

        
        """
        body = {
            "user_name": "user2",
            "first_name": "user2",
            "last_name": "user2",
            "email": "user2@user.com",
            "phone": "9923929292",
            "password": "user2"
            }
        response = self.client.open(
            '/userservice/v1/users',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        
        
        
    def test_delete_user_return200(self):
        """Test case for delete_user

        
        """
        
        

        response = self.client.open(
            '/userservice/v1/users/{user_id}'.format(user_id="94a1b4777f0947d9a509e1c8fbb3c389"),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        
    def test_delete_user_return404(self):
        """Test case for delete_user

        
        """
        
        

        response = self.client.open(
            '/userservice/v1/users/{user_id}'.format(user_id="94a1b4777f0947d9a509e1c8fbb3c389"),
            method='DELETE')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    

    def test_get_user_details200(self):
        """Test case for get_user_details

        
        """
        response = self.client.open(
            '/userservice/v1/users/{user_id}'.format(user_id='680bec8d597c48dfa41e4eb7522756de'),
            method='GET')
        print(response)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_user_return200(self):
        """Test case for login_user

        
        """
        body = body = {
                        "user_id": "dd40c50041f74519857d008c47f63a77",
                        "user_name": "user6",
                        "password": "user6"
                        }
        response = self.client.open(
            '/userservice/v1/users/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        
    def test_login_user_return401(self):
        """Test case for login_user

        
        """
        body = body = {
                        "user_id": "dd40c50041f74519857d008c47f63a77",
                        "user_name": "user6",
                        "password": "user6"
                        }
        response = self.client.open(
            '/userservice/v1/users/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert401(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_login_user_return400(self):
        """Test case for login_user

        
        """
        body = body = {
                        "user_id": "dd40c50041f74519857d008c47f",
                        "user_name": "user6",
                        "password": "user6"
                        }
        response = self.client.open(
            '/userservice/v1/users/login',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert400(response,
                       'Response body is : ' + response.data.decode('utf-8'))



    def test_logout_user_return200(self):
        """Test case for logout_user

        
        """
        body={
            "token":"47c406ac29d5492cade357f4261eb433"
        }
        response = self.client.open(
            '/userservice/v1/users/logout',
            method='POST',
            data= json.dumps(body),
            content_type ='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_logout_user_return404(self):
        """Test case for logout_user

        
        """
        body={
            "token":"47c406ac29d5492cade357f4261eb433"
        }
        response = self.client.open(
            '/userservice/v1/users/logout',
            method='POST',
            data= json.dumps(body),
            content_type ='application/json')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    def test_update_user_data_return200(self):
        """Test case for update_user_data

        
        """
        body = {
            "user_name":"user5"
        }
        response = self.client.open(
            '/userservice/v1/users/{user_id}'.format(user_id='680bec8d597c48dfa41e4eb7522756de'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))
        
    def test_update_user_data_return500(self):
        """Test case for update_user_data

        
        """
        body = {
                "user_name":"user12",
                }
        response = self.client.open(
            '/userservice/v1/users/{user_id}'.format(user_id='680bec8d597c48dfa41e4eb7522756de'),
            method='PATCH',
            data=json.dumps(body),
            content_type='application/json')
        self.assert500(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    def test_get_all_users(self):
        """Test case for users_get

        
        """
        response = self.client.open(
            '/userservice/v1/users',
            method='GET')
        print(response)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_validate_user_token(self):
        """Test case for validate_user_token

        
        """
        body = {
            "token" : "eab5954d16024f22bb1e50da48a7d985"
            }
        response = self.client.open(
            '/userservice/v1/users/validate',
            method='POST',
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


    
    


if __name__ == '__main__':
    import unittest
    unittest.main()

