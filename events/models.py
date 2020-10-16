from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock

from wagtailcodeblock.blocks import CodeBlock


class EventListPage(Page):
    ''' Displays a lists of EventPage '''
    description = models.CharField(max_length=255, blank=True,)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full")
    ]

    def get_context(self, request, *args, **kwargs):
        ''' Used for adding menu items'''
        context = super(EventListPage, self).get_context(request, *args, **kwargs)
        context['menuitems'] = Page.objects.filter(
            live=True, show_in_menus=True)
        context['events'] = EventPage.objects.filter(
            live=True).order_by('-date')
        return context

    subpage_types = ['events.EventPage']


class EventPage(Page):
    ''' Event page content '''
    date = models.DateField('Fecha publicación')
    is_meetup = models.BooleanField('Evento de meetup', default=False)
    event_url = models.URLField('URL', max_length=250, blank=True, null=True)
    description = models.TextField('Descripción', blank=True)
    image = models.ImageField('Imagen principal', blank=True, null=True)
    meetup_image_url = models.URLField('Meetup image url', blank=True, null=True)

    editor_features = ['h2', 'h3', 'h4', 'bold', 'italic', 'link', 'code',
                       'ol', 'ul', 'hr', 'document-link', 'image', 'embed',
                       'strikethrough', 'blockquote']
    body = StreamField([
        ('heading', blocks.CharBlock(classname='full title')),
        ('paragraph', blocks.RichTextBlock(features=editor_features)),
        ('code', CodeBlock(label='Code')),
        ('image', ImageChooserBlock()),

    ], blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname='full'),
        FieldPanel('date'),
        FieldPanel('image'),
        StreamFieldPanel('body')
    ]

    def get_context(self, request, *args, **kwargs):
        ''' Used for adding menu items '''
        context = super(EventPage, self).get_context(request, *args, **kwargs)
        context['menuitems'] = Page.objects.filter(
            live=True, show_in_menus=True)
        return context

    subpage_types = []
