"""Django command to wait for db"""

import time

from psycopg2 import OperationalError as Psycopg2OpError


from django.db import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """ DJANGO COMMAND TO WAIT FOR DATABASE """
    
    def handle(self, *args, **options):
        """ENTRY POINT FOR COMMAND"""
        self.stdout.write('Waiting for database...')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
       