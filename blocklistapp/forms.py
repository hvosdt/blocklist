from .models import Item
from django.forms import ModelForm

class ItemForm (ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'rank')

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })