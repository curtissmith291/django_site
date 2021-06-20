"""my_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from theblog.views import BlogView, ArticleDetailView
# from theblog.views import blog_view
from django.contrib import admin
from django.urls import path
from pages.views import home_view, scratch_view, about_view, projects_view, square_view, hello_form

# Note: the "name" attribute is how the url is referenced
urlpatterns = [
    path('', home_view, name = 'home'),          # http://127.0.0.1:8000/ is the same as the home page below
    path('home/', home_view, name = 'home'),     # website home page
    path('scratch/', scratch_view, name = 'scratch'),     # to test html
    path('about/', about_view, name = 'about'),
    path('projects/', projects_view, name = 'projects'),
    path('square/', square_view, name = 'square'),
    path ('hello/', hello_form, name="hello"),
    path('admin/', admin.site.urls),
    path('blog/', BlogView.as_view(), name='blog'),  # need to call "as_view" since it's a class based view
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    # path('blog/', blog_view, name='blog'),
]