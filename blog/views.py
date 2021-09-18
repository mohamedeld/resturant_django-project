from django.shortcuts import render,get_object_or_404
from .models import Post,Category,Comment
from taggit.models import Tag
from .forms import CommentForm
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
def post_list(request):
   post_list= Post.objects.all()

   search_query= request.GET.get('q')
   if search_query:
      post_list = post_list.filter(
         Q(title__icontains = search_query)|
         Q(content__icontains = search_query)|
         Q(tags__name__icontains = search_query)
      ).distinct()
   paginator = Paginator(post_list, 9) # Show 25 contacts per page.
   page = request.GET.get('page')
   post_list = paginator.get_page(page)

   return render(request,'blog/post_list.html',{
      'post_list':post_list,
   })

def post_detail(request,id):
   post_detail = get_object_or_404(Post,id=id)
   categories = Category.objects.all()
   all_tags = Tag.objects.all()
   comments = Comment.objects.filter(post=post_detail)
   comment_form = CommentForm()
   if request.method == 'POST':
      comment_form = CommentForm(request.POST)
      if comment_form.is_valid():
         new_comment = comment_form.save(commit=False)
         new_comment.user = request.user
         new_comment.post = post_detail
         new_comment.save()
      else:
         comment_form = CommentForm()

   return render(request,'blog/post_detail.html',{
      'post_detail':post_detail,
      'categories':categories,
      'all_tags':all_tags,
      'comments':comments,
      'comment_form':comment_form,
   })

def post_by_tag(request,tag):
   post_by_tag = Post.objects.filter(tags__name__in = [tag])
   return render(request,'blog/post_list.html',{
      'post_list':post_by_tag,
   })

def post_by_category(request,category):
   post_by_category = Post.objects.filter(category__category_name = [category])
   return render(request,'blog/post_list.html',{
      'post_list':post_by_category,
   })