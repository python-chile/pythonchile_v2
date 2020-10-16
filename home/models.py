from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, \
    InlinePanel
from wagtail.core import blocks
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtailcodeblock.blocks import CodeBlock

from blog.models import PostPage


class ImageItem(models.Model):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    url = models.URLField("URL", blank=True)
    description = models.CharField("Descripción", max_length=500, blank=True)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('url'),
        FieldPanel('description'),
    ]

    class Meta:
        abstract = True


class HomePage(Page):

    def get_context(self, request, *args, **kwargs):
        ''' Used for adding menu items to home'''
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['menuitems'] = Page.objects.filter(
            live=True, show_in_menus=True)
        context['blog_posts'] = PostPage.objects.filter(
            live=True).order_by('-date')[:5]

        return context

    subpage_types = [
        'blog.BlogPage',
        'events.EventListPage',
        'home.GeneralPage',
        'home.CommunityPage'
    ]


class GeneralPage(Page):
    ''' Multiuse page for general content '''
    description = models.CharField("Descripción", max_length=255, blank=True)
    image = models.ImageField("Imagen principal", blank=True, null=True)

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('code', CodeBlock(label='Code')),
        ('image', ImageChooserBlock()),

    ], blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        FieldPanel('image'),
        StreamFieldPanel('body')
    ]

    def get_context(self, request, *args, **kwargs):
        ''' Used for adding menu items '''
        context = super(GeneralPage, self).get_context(
            request, *args, **kwargs)
        context['menuitems'] = Page.objects.filter(
            live=True, show_in_menus=True)
        return context

    subpage_types = []


class CommunityPageTeamItem(Orderable, ImageItem):
    page = ParentalKey('home.CommunityPage', related_name='team_profiles')
    name = models.CharField("Nombre", max_length=255, blank=True)

    panels = [
        FieldPanel('name'),
        # ImageItem fields
        ImageChooserPanel('image'),
        FieldPanel('description'),
        FieldPanel('url'),
    ]


class CommunityPage(Page):
    ''' Multiuse page for general content '''
    description = models.CharField("Descripción", max_length=255, blank=True)
    image = models.ImageField("Imagen principal", blank=True, null=True)

    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('code', CodeBlock(label='Code')),
        ('image', ImageChooserBlock()),
    ], blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('description', classname="full"),
        FieldPanel('image'),
        StreamFieldPanel('body'),
        InlinePanel('team_profiles', label="Perfil equipo"),
    ]

    def get_context(self, request, *args, **kwargs):
        ''' Used for adding menu items '''
        context = super(CommunityPage, self).get_context(
            request, *args, **kwargs)
        context['menuitems'] = Page.objects.filter(
            live=True, show_in_menus=True)
        return context

    subpage_types = []
