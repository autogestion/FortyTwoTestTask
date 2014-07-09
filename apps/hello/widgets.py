from django.conf import settings
from django import forms
from django.utils.safestring import mark_safe


class Calendar(forms.TextInput):

    class Media:
        js = (
            settings.STATIC_URL + 'js/libs/jquery-1.11.1.min.js',
            settings.STATIC_URL + 'jquery-ui-1.11.0.custom/js/' +
            'jquery-ui-1.11.0.custom.min.js',)
        css = {
            'all': (settings.STATIC_URL + 'jquery-ui-1.11.0.custom/' +
                    'development-bundle/themes/ui-lightness/jquery-ui.css',)
        }

    def __init__(self, params='', attrs={}):
        self.params = params
        super(Calendar, self).__init__()

    def render(self, name, value, attrs=None):
        base = super(Calendar, self).render(name, value, attrs=attrs)
        return base + mark_safe(u'''<script type="text/javascript">
                                $("#id_%s").datepicker({%s});
                                $("#id_%s").attr('readonly', true);
                                </script>'''%(name, self.params, name,))
