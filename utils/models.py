from wagtail.core.models import Page


class CustomPage(Page):
    '''
    CustomPage model to extend from other Pages
    '''
    def get_context(self, request, *args, **kwargs):
        ''' Used for adding menu items'''
        context = super(CustomPage, self).get_context(
            request, *args, **kwargs)
        context['menuitems'] = Page.objects.filter(
            live=True, show_in_menus=True)
        return context

    class Meta:
        abstract = True
