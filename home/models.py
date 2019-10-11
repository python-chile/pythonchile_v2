from wagtail.core.models import Page


class HomePage(Page):
    pass

    def get_context(self, request, *args, **kwargs):
        ''' Used for adding menu items to home'''
        context = super(HomePage, self).get_context(request, *args, **kwargs)
        context['menuitems'] = self.get_children().filter(
            live=True, show_in_menus=True)

        return context
