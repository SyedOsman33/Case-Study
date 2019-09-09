from django.db import models

# Create your models here.



class PhoneNumbers(models.Model):
    number = models.CharField(max_length=20, blank=True, null=True)

    def to_json(self):
        return {
            "id": self.id,
            "number": self.number
        }


class Emails(models.Model):
    email = models.CharField(max_length=100, blank=True, null=True)

    def to_json(self):
        return {
            "id": self.id,
            "email": self.email
        }


class UserManagment(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    emails = models.ManyToManyField(Emails, blank=True, null=True)
    phone_numbers = models.ManyToManyField(PhoneNumbers, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " +self.last_name

    def to_json(self):
        phone_num_list = [ph_num.to_json() for ph_num in self.phone_numbers.all()]
        emails_list = [email.to_json() for email in self.emails.all()]

        return {
            "id": self.id,
            "name": self.first_name + " " +self.last_name,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "emails": emails_list,
            "phone_numbers": phone_num_list,
        }
