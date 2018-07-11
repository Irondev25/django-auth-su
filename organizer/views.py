from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (View, ListView, DetailView,
                                  DeleteView, CreateView)
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator

from .models import Tag, Startup, Newslink
from .forms import TagForm, NewslinkForm, StartupForm
from .utils import (PageLinkMixin, StartupContextMixin, NewslinkGetObjectMixin)
from core.utils import UpdateView
from user.decorators import required_authenticated_permissions


#views relate to Tag.
class TagList(PageLinkMixin, ListView):
    model = Tag
    paginate_by = 5


class TagDetail(DetailView):
    model = Tag


@required_authenticated_permissions('organizer.add_tag')
class TagCreate(CreateView):
    form_class = TagForm
    template_name = 'organizer/tag_form.html'


@required_authenticated_permissions('organizer.change_tag')
class TagUpdate(UpdateView):
    model = Tag
    form_class = TagForm

@required_authenticated_permissions('organizer.delete_tag')
class TagDelete(DeleteView):
    model = Tag
    success_url = reverse_lazy('organizer:tag_list')


#views relate to startup
class StartupList(PageLinkMixin, ListView):
    model = Startup
    paginate_by = 5


class StartupDetail(DetailView):
    model = Startup

@required_authenticated_permissions('organizer.add_startup')
class StartupCreate(CreateView):
    form_class = StartupForm
    template_name = 'organizer/startup_form.html'

@required_authenticated_permissions('organizer.change_update')
class StartupUpdate(UpdateView):
    form_class = StartupForm
    model = Startup

@required_authenticated_permissions('oranizer.delete_startup')
class StartupDelete(DeleteView):
    model = Startup
    success_url = reverse_lazy('organizer:startup_list')

#views relate to Newslink


@required_authenticated_permissions('oranizer.create_newslink')
class NewslinkCreate(NewslinkGetObjectMixin, StartupContextMixin, CreateView):
    form_class = NewslinkForm
    template_name = 'organizer/newslink_form.html'
    model = Newslink

    def get_initial(self):
        startup_slug = self.kwargs.get(
            self.startup_slug_url_kwarg
        )
        self.startup = get_object_or_404(
            Startup,
            slug__iexact=startup_slug
        )
        initial = {
            self.startup_context_object_name: self.startup
        }
        initial.update(self.initial)
        return initial

@required_authenticated_permissions('organizer.change_newslink')
class NewslinkUpdate(NewslinkGetObjectMixin, StartupContextMixin, UpdateView):
    form_class = NewslinkForm
    model = Newslink
    slug_url_kwarg = 'newslink_slug'

@required_authenticated_permissions('organizer.delete_newslink')
class NewslinkDelete(NewslinkGetObjectMixin ,StartupContextMixin, DeleteView):
    model = Newslink
    slug_url_kwarg = 'newslink_slug'
  
