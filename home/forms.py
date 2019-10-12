from django.forms import Form
from django.contrib.auth.models import Group


class EditorSignupForm(Form):
    ''' Form used to add registered users to Editors group '''
    pass

    def signup(self, request, user):
        role = request.session.get('user_type')
        group_name = role or "Editors"
        group = Group.objects.get(name=group_name)
        user.groups.add(group)
        user.save()
