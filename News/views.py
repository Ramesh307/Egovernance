from django.shortcuts import render,redirect
from News.models import Post,Category,Comments
from News.forms import CommentForm
from django.views.generic import ListView
from django.db.models import Q
# Create your views here.
def homepage(request):
    post=Post.objects.filter(IsActive=True)
    category = Category.objects.filter(IsActive=True)
    comments = Comments.objects.filter()
    commentForm = CommentForm
    return render(request, "home.html",{'post':post,'category':category,'commentForm':commentForm,'comments':comments})

def savecomments(request):
    if request.method == "POST":
        Fullname=request.POST['Fullname']
        Email=request.POST['Email']
        details=request.POST['details']
        comment=Comments.objects.create(Fullname=Fullname,Email=Email,details=details)
    return redirect("home")

def categoryfilter(request,category_id):
    category = Category.objects.filter(id=category_id)
    return render(request,"category_result.html",{'category':category})



def newsfilter(request,post_id):
    post = Post.objects.filter(id=post_id)
    return render(request,"news_result.html",{'posts':post})

class SearchResultsListView(ListView):
    model = Post
    context_object_name = 'result'
    template_name = 'search_result.html'
    def get_queryset(self):
       query = self.request.GET.get('q')
       return Post.objects.filter(
        Q(Title__icontains=query))
       
       
def about(request):
    return render(request,"aboutus.html")