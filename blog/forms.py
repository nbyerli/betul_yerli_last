from django import forms

from blog.models import BlogEntry


class BlogEntryForm(forms.ModelForm):

    class Meta:
        model = BlogEntry
        fields = ["title", "body", "tag", "user"]