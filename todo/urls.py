"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from users.api.urls import router as user_router
from tasks.api.urls import router as task_router
from shopping.api.urls import router as shopping_router
from budget.api.urls import router as budget_router

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += user_router.urls
urlpatterns += task_router.urls
urlpatterns += shopping_router.urls
urlpatterns += budget_router.urls
