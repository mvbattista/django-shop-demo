# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
try:
    from StringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO
from django.conf import settings
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.utils.translation import ugettext_lazy as _
try:
    import czipfile as zipfile
except ImportError:
    import zipfile


class Command(BaseCommand):
    help = _("Initialize the workdir to run the demo of giftshop.")

    def add_arguments(self, parser):
        parser.add_argument(
            '--noinput', '--no-input',
            action='store_false',
            dest='interactive',
            default=True,
            help="Do NOT prompt the user for input of any kind.",
        )

    def set_options(self, **options):
        self.interactive = options['interactive']

    def handle(self, verbosity, *args, **options):
        self.set_options(**options)
        call_command('migrate')
        initialize_file = os.path.join(settings.WORK_DIR, '.initialize')
        if os.path.isfile(initialize_file):
            self.stdout.write("Initializing project giftshop")
            call_command('makemigrations', 'giftshop')
            call_command('migrate')
            os.remove(initialize_file)
            call_command('loaddata', 'skeleton')
            call_command('shop', 'check-pages', add_recommended=True)
            call_command('assign_iconfonts')
            call_command('create_social_icons')
            call_command('download_workdir', interactive=self.interactive)
            call_command('loaddata', 'products-media')
            call_command('import_products')
        else:
            self.stdout.write("Project giftshop already initialized")
            call_command('migrate')
