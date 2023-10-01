from django import forms

from .models import Comment


class CommentForm(forms.ModelForm):
    """Форма создания комментария к задаче."""

    class Meta:
        model = Comment
        fields = ('text',)
