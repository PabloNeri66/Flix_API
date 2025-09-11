from actors.models import Actor
from datetime import datetime
from django.core.management.base import BaseCommand
import csv
import logging


logger = logging.getLogger('flix_api')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='Nome do arquivo',
        )

    def handle(self, *args, **options):
        file_name = options['file_name']
        logger.info('Processo de cadastro de atores iniciado... ')

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    name = row['name']
                    birthday = datetime.strptime(
                        row['birthday'],
                        format='%Y/%m/%d',
                    ).date()
                    nationality = row['nationality']
                    logger.info(f'Ator {name} em processo de cadastro...')

                    if name and Actor.objects.filter(name=name).exists():
                        logger.info(f'{name} já cadastrado!')
                        continue

                    Actor.objects.create(
                        name=name,
                        birthday=birthday,
                        nationality=nationality,
                    )

                except Exception as e:
                    logger.error(f'Erro ao processar cadastro {e}')
            logger.info('Processo de cadastro de atores Terminado.')
