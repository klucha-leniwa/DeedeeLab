from django.forms import ModelForm
from models import Comment


class CommentForm(ModelForm):
    """Class for comment form. Contains set_initial method which sets initial
    values for each fields in form. Private attribute __form_final_values stores
    values for fields that have initial values"""


    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Comment
        exclude = ('created_at', 'comment_title', 'post')
