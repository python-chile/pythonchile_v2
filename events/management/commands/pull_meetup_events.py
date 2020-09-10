from django.core.management.base import BaseCommand, CommandError
from events.tasks import pull_meetup_events


class Command(BaseCommand):
    ''' Custom command used to pull events data from Meetups groups '''
    help = 'Pulls events from meetup'

    def handle(self, *args, **options):

        meetup_anlytics_python = 'https://www.meetup.com/es-ES/Analytics-y-Python/events/'
        meetup_python_101 = 'https://www.meetup.com/es-ES/python101/events/'

        meetups_array = [meetup_anlytics_python, meetup_python_101, ]
        print(f'Pulling events from: {meetups_array}')

        try:
            pull_meetup_events(meetups_array)
        except Exception as e:
            print(e)
            raise CommandError(e)

        self.stdout.write(self.style.SUCCESS(
            'Successfully pulled meetup events'))
