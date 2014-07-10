from django import template
from django.core.urlresolvers import reverse
from django.contrib.contenttypes.models import ContentType


register = template.Library()


@register.simple_tag
def edit_link(user):
    cont_type = ContentType.objects.get_for_model(user)
    return '<a href="%s">(admin)</a>' \
           % reverse('admin:%s_%s_change'
           % (cont_type.app_label, cont_type.model), args=[user.id])