import json
import traceback

from django.db.models import Q
from django.http import HttpResponse

from user_managment.constants import ERROR_PARAMS_MISSING_BODY
from .models import UserManagment, PhoneNumbers, Emails



def exception_handler(def_value=None):
    def decorate(f):
        def applicator(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as err:
                return def_value
        return applicator
    return decorate


def verify_request_params(params):
    def decorator(func):
        def inner(request, *args, **kwargs):
            if not all(param in request.query_params for param in params):
                return generic_response(response_body=ERROR_PARAMS_MISSING_BODY, http_status=200)
            return func(request, *args, **kwargs)
        return inner
    return decorator


def generic_response(response_body, http_status=200, header_dict={}, mime='application/json'):
    from django.core.serializers.json import DjangoJSONEncoder
    msg = json.dumps(response_body, cls=DjangoJSONEncoder)
    resp = HttpResponse(msg, status=http_status, content_type=mime)
    for name, value in header_dict.items():
        resp[name] = value
    return resp


def get_users_by_name(name):
    users_list = UserManagment.objects.filter(Q(first_name__icontains=name) | Q(last_name__icontains=name))
    print(users_list)
    final_list = [user.to_json() for user in users_list]
    return final_list


def get_user_by_id(user_id):
    try:
        user_obj = UserManagment.objects.get(pk=user_id)
    except UserManagment.DoesNotExist:
        user_obj = None

    return user_obj.to_json() or "No User Found"


def add_additional_user_contact_info(user_id, user_phone, user_email):
    try:
        user_obj = UserManagment.objects.get(pk=user_id)
    except UserManagment.DoesNotExist:
        return "User Not Found"

    if user_obj:
        if user_phone:
            user_obj.phone_numbers.create(number=user_phone)
        if user_email:
            user_obj.emails.create(email=user_email)

        user_obj.save()

        return user_obj.to_json()
    else:
        return False

def edit_users_contact_info(user_id, email_id, phone_id, new_phone_num, new_email):
    try:
        user_obj = UserManagment.objects.get(pk=user_id)
    except UserManagment.DoesNotExist:
        return "User Not Found"

    if user_obj:
        try:
            if email_id:
                exsiting_email = user_obj.emails.get(pk=email_id)
                exsiting_email.email = new_email
                exsiting_email.save()
            if phone_id:
                exsiting_phone = user_obj.phone_numbers.get(pk=phone_id)
                exsiting_phone.number = new_phone_num
                exsiting_phone.save()

            return user_obj.to_json()
        except:
            return False
    else:
        return False

def edit_users_data(user_id, **data):
    if data:
        try:
            user_obj = UserManagment.objects.filter(pk=user_id)
            user_obj.update(**data)
            return user_obj[0].to_json()
        except UserManagment.DoesNotExist or UserManagment.MultipleObjectsReturned:
            traceback.print_exc()
            return "User Not Found"
    else:
        return False


def create_users_data(data):
    try:
        phone_num_list = []
        emails_list = []

        user_obj = UserManagment()
        user_obj.first_name = data.get('first_name')
        user_obj.last_name = data.get('last_name')
        user_obj.save()

        if data.getlist("phone_numbers"):
            phn_numbers = data.get("phone_numbers").split(',')
            for number in phn_numbers:
                phone_numbs = PhoneNumbers.objects.create(number=number.strip())
                phone_num_list.append(phone_numbs)

        if data.getlist("emails"):
            usr_emails = data.get("emails").split(',')
            for email in usr_emails:
                emails = Emails.objects.create(email=email.strip(" "))
                emails_list.append(emails)

        user_obj.phone_numbers.add(*phone_num_list)
        user_obj.emails.add(*emails_list)

        return user_obj.to_json()

    except Exception as e:
        traceback.print_exc()
        return False


def delete_user_data(user_id):
    if user_id:
        try:
            user_obj = UserManagment.objects.get(pk=user_id)
            user_obj.phone_numbers.all().delete()
            user_obj.emails.all().delete()
            user_obj.delete()
            return "Deleted"
        except UserManagment.DoesNotExist:
            traceback.print_exc()
            return "No user Found"
    else:
        return False
