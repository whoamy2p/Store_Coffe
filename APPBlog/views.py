
from django.shortcuts import render, redirect
from APPBlog.models import Categoria, Post

# Create your views here.
def blog_post (request):
    global data
    data=Categoria.objects.all ()
    post=Post.objects.all ()


    return render (request, "APPBlog/blog.html", {"Data_blog": data, "post":post})

def categorias_post (request, categoria_id):
    if categoria_id == 1:
        return redirect ("/Blog")
    
    else:
        data=Categoria.objects.filter (id=1)
        category=Post.objects.filter (catagoria=categoria_id)

        return render (request, "APPBlog/categorias.html", {"Category_data":category, "Data_blog": data})

