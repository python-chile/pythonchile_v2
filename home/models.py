from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.core import blocks
from wagtail.core.models import Page
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtailcodeblock.blocks import CodeBlock

from blog.models import PostPage


class HomePage(Page):

    def get_context(self, request, *args, **kwargs):
        ''' Used for adding menu items to home'''
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['menuitems'] = Page.objects.filter(
            live=True, show_in_menus=True)
        context['blog_posts'] = PostPage.objects.filter(
            live=True).order_by('-date')[:5]

        return context


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
