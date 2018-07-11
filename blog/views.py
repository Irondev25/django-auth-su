from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy

# Create your views here.
from django.views.generic import (ListView, CreateView, UpdateView, DetailView,
                                    YearArchiveView, ArchiveIndexView, MonthArchiveView,
                                    DateDetailView, DeleteView)
from django.views.decorators.http import require_http_methods
from django.shortcuts import render, get_object_or_404


from .models import Post
from .forms import PostForm
from organizer.utils import PageLinkMixin
from .utils import DateObjectMixin, AllowFuturePermissionMixin
from user.decorators import required_authenticated_permissions

# def post_list(request):
#     return render(request, 'blog/post_list.html', {'post_list':Post.objects.all()})

class PostList(AllowFuturePermissionMixin ,PageLinkMixin ,ArchiveIndexView):
    model = Post
    allow_empty = True
    context_object_name = 'post_list'
    date_field = 'pub_date'
    paginate_by = 5
    template_name_suffix = '_list'
    make_object_list = True


class PostArchiveYear(AllowFuturePermissionMixin ,YearArchiveView):
    model = Post
    date_field = 'pub_date'
    make_object_list = True


class PostArchiveMonth(AllowFuturePermissionMixin ,MonthArchiveView):
    model = Post
    date_field = 'pub_date'
    month_format = "%m"

# @require_http_methods(['GET', 'HEAD'])
# def post_detail(request, year, month, slug):
#     post = get_object_or_404(Post, pub_date__year=year, pub_date__month=month, slug=slug)
#     return render(
#         request,
#         'blog/post_detail.html',
#         {'post':post}
#     )


class PostDetail(DateObjectMixin ,DetailView):
    model = Post


@required_authenticated_permissions('blog.add_post')
class PostCreate(CreateView):
    template_name = 'blog/post_form.html'
    form_class = PostForm

@required_authenticated_permissions('blog.change_post')
class PostUpdate(DateObjectMixin ,UpdateView):
    template_name = 'blog/post_update_form.html'
    form_class = PostForm
    model = Post
        
@required_authenticated_permissions('blog.delete_post')
class PostDelete(DateObjectMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')
