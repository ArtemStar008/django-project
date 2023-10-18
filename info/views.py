from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from info.models import InfoBlog


# Create your views here.

def read_post(request):
    return render(request, 'index.html')


def second_page(request):
    return render(request, 'second_page.html')


def third_page(request):
    return render(request, 'third_page.html')


class PostsView(View):
    def get(self, request, id=None):
        posts = InfoBlog.objects.filter(is_deleted=False)  # запрос подготовился

        if id:
            post = InfoBlog.objects.filter(id=id, is_deleted=False).first()
            return render(request, 'post.html', context={'post': post, 'posts': posts})

        return render(request, 'db_admin.html', context={'posts': posts})

        # # print(posts.query)
        # # print(amount_posts)
        # return render(request, 'db_admin.html', context={
        #     # 'amount_posts': posts,
        #     'posts': posts,
        # })  # запрос пошел в базу

# {'amount_posts_name': amount_posts_value}
