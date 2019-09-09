from django.shortcuts import render
from rest_framework.decorators import api_view
from user_managment.constants import *
from user_managment.utils import *
# Create your views here.



@api_view(['GET'])
@exception_handler(generic_response(response_body=ERROR_RESPONSE_BODY, http_status=500))
def get_user_by_id(request, id):
    response_body = {RESPONSE_MESSAGE: DEFAULT_ERROR_MESSAGE, RESPONSE_DATA: {}}
    http_status = 500

    user = get_user_id(id)

    if user:
        http_status = 200
        response_body[RESPONSE_MESSAGE] = SUCCESS
        response_body[RESPONSE_DATA] = user

    return generic_response(response_body=response_body, http_status=http_status)


@api_view(['GET'])
@verify_request_params(params=['name'])
@exception_handler(generic_response(response_body=ERROR_RESPONSE_BODY, http_status=500))
def find_users_by_name(request):
    response_body = {RESPONSE_MESSAGE: DEFAULT_ERROR_MESSAGE, RESPONSE_DATA: {}}
    http_status = 500

    name = request.GET.get("name", None)

    create_user = get_users_by_name(name=name)

    if create_user:
        http_status = 200
        response_body[RESPONSE_MESSAGE] = SUCCESS
        response_body[RESPONSE_DATA] = create_user

    return generic_response(response_body=response_body, http_status=http_status)


@api_view(['POST'])
@verify_request_params(params=['first_name', 'last_name', 'emails', 'phone_numbers'])
@exception_handler(generic_response(response_body=ERROR_RESPONSE_BODY, http_status=500))
def add_user(request):
    response_body = {RESPONSE_MESSAGE: DEFAULT_ERROR_MESSAGE, RESPONSE_DATA: {}}
    http_status = 500

    create_user = create_users_data(request.data)

    if create_user:
        http_status = 200
        response_body[RESPONSE_MESSAGE] = "User Added Sucessfully"
        response_body[RESPONSE_DATA] = create_user

    return generic_response(response_body=response_body, http_status=http_status)


@api_view(['PATCH'])
@verify_request_params(params=['id'])
@exception_handler(generic_response(response_body=ERROR_RESPONSE_BODY, http_status=500))
def edit_users(request):
    response_body = {RESPONSE_MESSAGE:DEFAULT_ERROR_MESSAGE, RESPONSE_DATA: {}}
    http_status = 500

    user_id = request.data.get("id", None)
    first_name = request.POST.get("first_name", None)
    last_name = request.POST.get("last_name", None)

    data = {"first_name": first_name, "last_name": last_name}

    create_user = edit_users_data(user_id, **data)

    if create_user:
        http_status = 200
        response_body[RESPONSE_MESSAGE] = SUCCESS
        response_body[RESPONSE_DATA] = create_user

    return generic_response(response_body=response_body, http_status=http_status)


@api_view(['POST'])
@verify_request_params(params=['id', 'email_id', 'phone_id', 'email', 'phone_number'])
@exception_handler(generic_response(response_body=ERROR_RESPONSE_BODY, http_status=500))
def edit_contact_info(request):
    response_body = {RESPONSE_MESSAGE: DEFAULT_ERROR_MESSAGE, RESPONSE_DATA: {}}
    http_status = 500

    user_id = request.data.get("id", None)
    email = request.POST.get("email", None)
    email_field_id = request.POST.get("email_id", None)
    phone = request.POST.get("phone_number", None)
    phone_field_id = request.POST.get("phone_id", None)


    create_user = edit_users_contact_info(user_id=user_id, email_id=email_field_id, new_email=email, phone_id=phone_field_id, new_phone_num=phone)

    if create_user:
        http_status = 200
        response_body[RESPONSE_MESSAGE] = SUCCESS
        response_body[RESPONSE_DATA] = create_user

    return generic_response(response_body=response_body, http_status=http_status)


@api_view(['POST'])
@verify_request_params(params=['id'])
@exception_handler(generic_response(response_body=ERROR_RESPONSE_BODY, http_status=500))
def add_additional_contact_info(request):
    response_body = {RESPONSE_MESSAGE: DEFAULT_ERROR_MESSAGE, RESPONSE_DATA: {}}
    http_status = 500

    user_id = request.data.get("id", None)
    email = request.POST.get("email", None)
    phone = request.POST.get("phone_number", None)


    create_user = add_additional_user_contact_info(user_id=user_id, user_phone=phone, user_email=email)

    if create_user:
        http_status = 200
        response_body[RESPONSE_STATUS] = True
        response_body[RESPONSE_MESSAGE] = SUCCESS
        response_body[RESPONSE_DATA] = create_user

    return generic_response(response_body=response_body, http_status=http_status)


@api_view(['DELETE'])
@exception_handler(generic_response(response_body=ERROR_RESPONSE_BODY, http_status=500))
def delete_user(request, id):
    response_body = {RESPONSE_MESSAGE: DEFAULT_ERROR_MESSAGE, RESPONSE_DATA: {}}
    http_status = 500

    # user_id = request.data.get("id", None)

    delete = delete_user_data(user_id=id)

    if delete:
        http_status = 200
        response_body[RESPONSE_MESSAGE] = delete

    return generic_response(response_body=response_body, http_status=http_status)
