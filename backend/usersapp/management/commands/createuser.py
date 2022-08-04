import getpass
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = (
        'This command create user'
        )

    def handle(self, *args, **options):
        user_model = get_user_model()
        username = input('Username: ')
        while True:
            passwd = getpass.getpass()
            passwd2 = getpass.getpass('Password (again): ')
            if passwd == passwd2:    
                new_user = user_model.objects.create_user(
                    username=username,
                    first_name=input('First name: '),
                    last_name=input('Last name: '),
                    email=input('Email: '),
                    password=passwd,
                )
                new_user.is_superuser = False
                new_user.is_staff = False
                new_user.save()
                break
