import os
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Renombra un proyecto Django'

    def add_arguments(self, parser):
        parser.add_argument('new_name', type=str, help='El nuevo nombre del proyecto')

    def handle(self, *args, **kwargs):
        new_name = kwargs['new_name']

        files_to_rename = ['djangoheroku/settings.py', 'djangoheroku/wsgi.py', 'manage.py', 'Procfile']
        folder_to_rename = 'djangoheroku'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace('djangoheroku', new_name)

            with open(f, 'w') as file:
                file.write(filedata)

        os.rename(folder_to_rename, new_name)

        self.stdout.write(self.style.SUCCESS('Proyecto ha sido renombrado a %s' % new_name))
