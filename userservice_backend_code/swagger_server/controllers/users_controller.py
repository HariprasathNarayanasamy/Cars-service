import connexion
import six
import uuid
from pymongo import MongoClient
from flask import jsonify , request
import ast
import json
import logging,logging.config

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
from swagger_server import util

cluster = MongoClient("localhost",27017)
carDatabase = cluster.carDatabase
users = carDatabase.users
userslogin = carDatabase.userslogin

logging.basicConfig(filename="newfile1.log",format="%(filename)s::%(levelname)s:%(message)s",level=logging.DEBUG)


def add_user(body=None):  # noqa: E501
    """add_user

    Add new user # noqa: E501

    :param body: Adding new user
    :type body: dict | bytes

    :rtype: Model201UserCreatedResponse
    """
    if connexion.request.is_json:
    #     body = UserInfo.from_dict(connexion.request.get_json())  # noqa: E501
    # else:
    #     message = "Bad request"
    #     return 400, message
        try:
            if users.find_one({"user_name":body['user_name']}):
                return "User already exist", 409
            else:
                body.update({"user_id" : (uuid.uuid4().hex)})
                users.insert_one(body)
                return "User Created", 200
        except:
            return "Internal_server_error",500


def delete_user(user_id):  # noqa: E501
    """delete_user

    delete users # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: Model200UserDeletedResponse
    """
    try:
        if users.find_one({"user_id":user_id}):
            delete_user = users.delete_one({"user_id":user_id})
            return "successfully deleted",200
        else:
            return "User_id is not found", 404
    except:
        return "Internal_server_error",500
    


def get_user_details(user_id):  # noqa: E501
    """get_user_details

    Get details of one user # noqa: E501

    :param user_id: 
    :type user_id: str

    :rtype: Model200UserDetailsResponse
    """
    try:
        data = users.find({"user_id":user_id})
        data_list=[]
        for i in data:
            i["_id"]=str(i["_id"])

            data_list.append(i)
        return data_list,200
    except:
        return "Internal_server_error",500

def login_user(body=None):  # noqa: E501
    """login_user

    login user # noqa: E501

    :param body: Login new user
    :type body: dict | bytes

    :rtype: LoginDetails
    """
    if connexion.request.is_json:
    #     print(type(body))
    #     body = LoginInfo.from_dict(connexion.request.get_json())  # noqa: E501
    # else:
    #     message = "Bad request"
    #     return 400, message
        try:
            if users.find_one({"user_id": body['user_id']}):
                if userslogin.find_one({"user_id":body['user_id']}):
                    return "user already logged in",401
                else:
                    body.update({"token_id" : (uuid.uuid4().hex)})
                    data = userslogin.insert_one(body)
                    return "User logged in", 200
            else:
                return "Invalid user", 401
        except:
            return "Internal_server_error",500


def logout_user(body=None):  # noqa: E501
    """logout_user

    logout user # noqa: E501
    :type body: dict | bytes


    :rtype: None
    """
    try:
        if userslogin.find_one({"token_id":body['token']}):
            delete_user = userslogin.delete_one({"token_id":body['token']})
            return "User logged out",200
        else:
            return "tokenId not found",404
    except:
            return "Internal_server_error",500


def update_user_data(user_id, body=None):  # noqa: E501
    """update_user_data

    Update one key of user details # noqa: E501

    :param user_id: 
    :type user_id: str
    :param body: Adds price and offers
    :type body: dict | bytes

    :rtype: Model200UpdateUserResponse
    """
    if connexion.request.is_json:
        body = UpdateUserInfo.from_dict(connexion.request.get_json())  # noqa: E501
    else:
        message = "Bad request"
        return 400, message
    try:
         body = ast.literal_eval(json.dumps(request.get_json()))
         users.update_many({"user_id":user_id},{"$set":body})
         return "successful",200
    
        
    except:
        return "Internal_server_error",500



def get_all_users():  # noqa: E501
    """users_get

    Get  all users # noqa: E501


    :rtype: UserDetails
    """
    try:
        data = users.find({},{"password":False})
        data_list = []
        for i in list(data):
            i["_id"]=str (i["_id"])
            data_list.append(i)
        return data_list,200

    except:
        return "Internal_server_error",500


def validate_user_token(body=None):  # noqa: E501
    """validate_user_token

    validate user token # noqa: E501

    :param body: Validate user token
    :type body: dict | bytes

    :rtype: Model200UserDetailsResponse
    """
    if connexion.request.is_json:
        # body = TokenInfo.from_dict(connexion.request.get_json())  # noqa: E501
        try:
            if userslogin.find_one({"token_id":body['token']}):
                return "User validated",200
            else:
                return "token_id is Not found",404
        except:
            return "Internal_server_error",500
