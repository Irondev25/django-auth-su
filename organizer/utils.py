from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django import forms
from django.views.generic import View

from .models import Startup, Newslink


class SlugCleanMixin:
    """Mixin class for slug cleaning method"""

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise forms.ValidationError("Slug can't be 'create'.")
        return new_slug


class PageLinkMixin:

    def _gen_page_url(self, page_number):
        return "?{pkw}={n}".format(
            pkw=self.page_kwarg,
            n=page_number
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        page = context.get('page_obj')
        context.update(
            {
                'previous_page_url': self.get_prev_url(page),
                'next_page_url': self.get_next_url(page),
                'page_kwarg': self.page_kwarg,
            }
        )
        return context

    def get_prev_url(self, page):
        if page.has_previous():
            page_number = page.previous_page_number()
            return self._gen_page_url(page_number)
        return None

    def get_next_url(self, page):
        if page.has_next():
            page_number = page.next_page_number()
            return self._gen_page_url(page_number)
        return None


class StartupContextMixin():
    startup_slug_url_kwarg = 'startup_slug'
    startup_context_object_name = 'startup'

    def get_context_data(self, **kwargs):
        if hasattr(self, 'startup'):
            context = {
                self.startup_context_object_name:self.startup
            }
        else:
            startup_slug = self.kwargs.get(self.startup_slug_url_kwarg)
            startup = get_object_or_404(Startup, slug__iexact=startup_slug)
            context = {
                self.startup_context_object_name: startup
            }
        context.update(kwargs)
        return super().get_context_data(**context)


class NewslinkGetObjectMixin():

    def get_object(self):
        startup_slug = self.kwargs.get(self.startup_slug_url_kwarg)
        newslink_slug = self.kwargs.get(self.slug_url_kwarg)
        return get_object_or_404(Newslink, slug__iexact=newslink_slug, startup__slug__iexact=startup_slug)