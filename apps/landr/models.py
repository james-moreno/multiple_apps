from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.
class RegManager(models.Manager):
    def new_reg(self, data):
        errors = []

        if not data['first_name']:
            errors.append("First Name can not be blank.")
        if not data['last_name']:
            errors.append("Last Name can not be blank.")
        if not data['email']:
            errors.append("Email can not be blank.")
        elif not EMAIL_REGEX.match(data['email']):
            errors.append("Invalid Email")
        if not data['password']:
            errors.append("Password can not be blank.")
        if not data['con_password']:
            errors.append("Confirm Password can not be blank.")
        if data['password'] != data['con_password']:
            errors.append("Passwords do not match.")

        response = {}
        if errors:
            response['errors'] = errors
            response['created'] = False
        else:
            password = data['password'].encode()
            hashed = bcrypt.hashpw(password, bcrypt.gensalt())
            print (hashed)
            new_user = self.create(first_name = data['first_name'], last_name = data['last_name'], email = data['email'], password = hashed)
            response['created'] = True
            response['new_user'] = new_user

        return response

    def login(self, data):
        print(data)
        errors = []

        if not data['log_email']:
            errors.append("No email was given.")
        if not data['log_password']:
            errors.append("No password was given.")

        response = {}
        if errors:
            response['errors'] = errors
            response['log_in'] = False

        else:
            user = Register.objects.get(email = data['log_email'])
            password = data['log_password'].encode()
            if bcrypt.hashpw(password, user.password.encode()):
                response['log_in'] = True
                response['user'] = user
        return response


class Register(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    objects = RegManager()
