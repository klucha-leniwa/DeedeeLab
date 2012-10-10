#encoding: utf-8


from django.http import HttpResponse
from django.template import Context, RequestContext, loader
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from forms import CommentForm
from models import Post, Category, Comment


def index(request):
    categories = Category.objects.all()
    post_list = Post.objects.all().order_by('-created_at')
    paginator = Paginator(post_list, 5)

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    template = loader.get_template('deedee/index.html')
    context = Context({
                       'posts': posts,
                       'categories': categories
                       })
    return HttpResponse(template.render(context))

def details(request, post_id):
    categories = Category.objects.all()
    commented_post = get_object_or_404(Post, id=post_id)
    comments_for_post = Comment.objects.filter(post_id=post_id).order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST,)
        if form.is_valid():
            comment_instance = form.save(commit=False)
            comment_instance.set_values(
                  comment_content=request.POST['comment_content'],
                  post=commented_post,
                  )
            comment_instance.save()
 
    else:
        form = CommentForm()

    try:
        previous_post = Post.objects.filter(
                                           category_id = commented_post.category_id,
                                           id__lt = commented_post.id
                                          ).order_by('-id')[0]
    except (Post.DoesNotExist, IndexError):
        previous_post = []

    try:
        next_post = Post.objects.filter(
                                           category_id = commented_post.category_id,
                                           id__gt = commented_post.id
                                          ).order_by('-id')[0]
    except (Post.DoesNotExist, IndexError):
        next_post = []

    template = loader.get_template('deedee/details.html')
    context = RequestContext(
                        request,
                        {
                       'post': commented_post,
                       'categories': categories,
                       'comments_for_post': comments_for_post,
                       'previous': previous_post,
                       'next': next_post,
                       'form': form,
                      })
    return HttpResponse(template.render(context))

def category(request, category_name):
    categories = Category.objects.all()
    category = get_object_or_404(Category, category_name = category_name)
    posts = Post.objects.filter(category_id = category.id)

    paginator = Paginator(posts, 5)

    page = request.GET.get('page')
    try:
        post = paginator.page(page)
    except PageNotAnInteger:
        post = paginator.page(1)
    except EmptyPage:
        post = paginator.page(paginator.num_pages)

    template = loader.get_template('deedee/category.html')
    context = Context ({
                        'category': category,
                        'categories': categories,
                        'posts': post
                       })
    return HttpResponse(template.render(context))

