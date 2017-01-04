from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from blog.forms import BlogEntryForm
from blog.models import BlogEntry


class EntryDetailView(DetailView):
    model = BlogEntry


class EntryListView(ListView):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(EntryListView, self).dispatch(*args, **kwargs)

    def get_queryset(self):
        qs = super(EntryListView, self).get_queryset()
        if not self.request.user.is_superuser:
            qs = qs.filter(user=self.request.user)
        elif "user_id" in self.kwargs:
            qs = qs.filter(user_id=self.kwargs["user_id"])
        return qs

    model = BlogEntry


class EntryCreateView(CreateView):
    template_name = "blog/blogentry_form.html"
    form_class = BlogEntryForm

    def get_success_url(self):
        return reverse('bloglist')
