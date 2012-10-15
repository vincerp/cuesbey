#encoding: utf-8
import sys
import os
import uuid
from django.core.management.base import BaseCommand, CommandError
from cuesbey_main.cube_viewer.models import Cube, make_and_insert_card, CardFetchingError

class Command(BaseCommand):
    args = "[FILENAME]+"
    help = ("import one or more cubes as a brand-new group of the cards "
            "specified in the provided file")

    def handle(self, *args, **options):

        for fpath in args:

            if not os.path.exists(fpath):
                raise CommandError('{} does not exist'.format(fpath))

            hash = uuid.uuid5(uuid.UUID('123456781234567812345678123AA1AA'), fpath)
            try:
                cube = Cube.objects.get(name=hash)
            except Cube.DoesNotExist:
                cube = Cube()
                cube.save()
                cube.name = hash

            with open(fpath, 'r') as cube_file:
                for card_name in cube_file:
                    if not card_name:
                        continue
                    try:
                        cube.add_card_by_name(card_name)
                    except CardFetchingError:
                        continue


            cube.save()