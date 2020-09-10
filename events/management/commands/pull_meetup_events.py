from django.core.management.base import BaseCommand, CommandError
from events.tasks import pull_meetup_events


class Command(BaseCommand):
    '''
    Custom command used to pull events data from Meetups groups
    Usage: ./manage.py pull_meetup_events
    Optional: Add --past True to pull all previous events.
    '''
    help = 'Pulls events from meetup'

    def add_arguments(self, parser):
        # Optional parameter to pull past events
        parser.add_argument(
            '--past',
            help='Pulls events from the past'
        )

    def handle(self, *args, **options):
        meetup_anlytics_python = 'https://www.meetup.com/es-ES/Analytics-y-Python/events/'
        meetup_python_101 = 'https://www.meetup.com/es-ES/python101/events/'
        meetups_array = [meetup_anlytics_python, meetup_python_101, ]

        if options['past']:
            # Append past to urls if past argument was found
            meetups_array = [
                meetup_url + 'past/' for meetup_url in meetups_array
            ]

        print(f'Pulling events from: {meetups_array}')
        try:
            pull_meetup_events(meetups_array)
        except Exception as e:
            print(e)
            raise CommandError(e)

        self.stdout.write(self.style.SUCCESS(
            'Successfully pulled meetup events'))
