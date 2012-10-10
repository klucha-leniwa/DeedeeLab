from django import forms
from django.db import models
from datetime import datetime


class ReadOnlyWidget(forms.Widget):
    def __init__(self, original_value, display_value):
        self.original_value = original_value
        self.display_value = display_value

        super(ReadOnlyWidget, self).__init__()

    def render(self, name, value, attrs=None):
        if self.display_value is not None:
            return unicode(self.display_value)
        return unicode(self.original_value)

    def value_from_datadict(self, data, files, name):
        return self.original_value

class CreatedAtField(models.Field):

    def __init__(self, *args, **kwargs):
        self.editable = False
        self.default = datetime.now()
        super(self.__class__, self).__init__()
