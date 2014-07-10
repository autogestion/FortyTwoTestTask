from django.core.management.base import BaseCommand, CommandError
from django.db import models
from optparse import make_option


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--error',
            action='store_true',
            dest='error',
            default=False,
            help='Dublicated output'),
    )

    @staticmethod
    def showmodels():
        info = ""
        for model in models.get_models():
            name = '%s.%s' % (
                model.__module__,
                model.__name__
            )
            number = model.objects.count()
            info += "model '%s' | count %d\n" % (name, number)
        return info

    def handle(self, *args, **options):
            info = self.showmodels()
            self.stdout.write(info)
            if options['error']:
                for line in info.split('\n'):
                    if line:
                        self.stderr.write('error: %s\n' % line)