from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = (
        'This command create superuser with default data \n'
        'login - DRF \n'
        'and some one test users without password'
        'Use comand like createtestusers arg(int)'
        )

    def add_arguments(self, parser) -> None:
        parser.add_argument('cnt', nargs='+', type=int)

    def handle(self, *args, **options):
        call_command('createsuperuser', '--username=DRF', '--email=admin@myproject.com')
        user_model = get_user_model()
        for i in range(*options['cnt']):
            new_user = user_model.objects.create_user(
                    username=f'TestUser{i}',
                    first_name=f'User first name {i}',
                    last_name=f'User last name {i}',
                    email=f'testemail{i}@mail.com',
                )
            new_user.is_superuser = False
            new_user.is_staff = False
            new_user.save()
