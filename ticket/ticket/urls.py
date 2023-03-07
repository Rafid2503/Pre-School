from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views,admin1,staff,student


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

#login path
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

#profile
    path('profile', views.PROFILE, name='profile'),
    path('profile/update', views.PROFILE_UPDATE, name='profile_update'),

# Admin panel
    path('admin1/home',admin1.HOME,name='admin_home'),
    path('admin1/student/add',admin1.ADD_STUDENT,name='add_student'),
    path('admin1/student/view',admin1.VIEW_STUDENT,name='view_student'),
    path('admin1/student/edit/<str:id>',admin1.EDIT_STUDENT,name='edit_student'),
    path('admin1/student/update',admin1.UPDATE_STUDENT,name='update_student'),

#Student Panel
    path('student/home',student.HOME,name='student_home'),




] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
