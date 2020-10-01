import requests
from datetime import datetime
from bs4 import BeautifulSoup

from .models import EventPage, EventListPage


def pull_meetup_events(meetup_urls):
    '''
    Main runner for pulling meetup events, called from a management command.
    See events/management/commands/pull_meetup_events.py
    '''
    for meetup_url in meetup_urls:
        print(f'\nPulling events from {meetup_url}...')
        events_data = _get_events_from_url(meetup_url)
        if events_data:
            print(f'\nCreatings events...')
            _create_events_pages(events_data)


def _get_events_from_url(meetup_url):
    ''' Requests next events for meetup groups '''

    print('--- Getting events from url ---')
    print(f'Trying to get events from {meetup_url}')
    # Call meetup_url
    event_list = []
    page = requests.get(meetup_url)
    if page.status_code == 200:
        # Parse page
        soup = BeautifulSoup(page.content, 'html.parser')
        events = soup.findAll('li', 'list-item border--none')
        for event in events:
            name = event.find(class_='eventCardHead--title').get_text()
            date = event.find('time').get('datetime')
            if len(event.findAll(class_='text--small padding--top margin--halfBottom')) > 0: 
                description = event.findAll(class_='text--small padding--top margin--halfBottom')[1].get_text()
            else:
                description = ''
            url = event.find(class_='eventCard--link').get('href')
            # Check if event haves an image
            if event.find(class_='eventCardHead--photo'):
                image = event.find(class_='eventCardHead--photo').get('style')
            # Append event data as a dict
            event_list.append({
                'name': name,
                'date': date,
                'url': url,
                'image': image,
                'description': description
            })
        return event_list

    else:
        print(f'- Error getting {url} -')

    print('--- Finished getting events ---')


def _create_events_pages(events):
    ''' Creates EventPage for every item from an incoming dictionary '''
    print(events)
    event_list = EventListPage.objects.first()
    for event in events:
        # Get or create event
        try:
            event_full_url = f'https://www.meetup.com/{event["url"]}'
            # Check if Event page exists
            existing_event = EventPage.objects.filter(event_url=event_full_url).first()
            image = _get_text_inside_parenthesis(event['image']) 
            if not existing_event:
                event_obj = EventPage(
                    event_url=event_full_url,
                    title=event['name'],
                    date=_timestamp_to_date_object(event['date']),
                    meetup_image_url=image,
                    description=event['description']
                )
                # Add as a eventlist child
                if event_list:
                    event_list.add_child(instance=event_obj)
            else:
                # TODO (CAVB): Update event data if already created
                print(f'Event page already created: {existing_event}')

        except KeyError as e:
            print(f'Error on updating/creating {event}')
            print(e)

    print('Finished creating events')


def _timestamp_to_date_object(timestamp):
    ''' Parses a string JS timestamp to a Python datetime object '''
    try:
        return datetime.fromtimestamp(int(timestamp) / 1000.0)
    except ValueError as e:
        print(f'Failed parsing timestamp to datetime object: {e}')
        return None

def _get_text_inside_parenthesis(string):
    ''' 
    Returns text inside a parenthesis.
    Example: lorem(text) -> text 
    '''
    # Note: if no parenthesis will return the original string
    return string[string.find("(")+1:string.find(")")]