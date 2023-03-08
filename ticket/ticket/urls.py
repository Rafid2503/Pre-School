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

# Admin panel(Rafid)
    path('admin1/home',admin1.HOME,name='admin_home'),
    path('admin1/student/add',admin1.ADD_STUDENT,name='add_student'),
    path('admin1/student/view',admin1.VIEW_STUDENT,name='view_student'),
    path('Admin1/Subject/Edit/<str:id>',admin1.EDIT_SUBJECT,name='edit_subject'),
    path('admin1/student/edit/<str:id>',admin1.EDIT_STUDENT,name='edit_student'),
    path('admin1/student/update',admin1.UPDATE_STUDENT,name='update_student'),
    path('admin1/student/delete<str:admin>',admin1.DELETE_STUDENT,name='delete_student'),
    path('admin1/course/add',admin1.ADD_COURSE,name='add_course'),
    path('admin1/course/view',admin1.VIEW_COURSE,name='view_course'),
    path('admin1/course/edit/<str:id>',admin1.EDIT_COURSE,name='edit_course'),
    path('admin1/course/update',admin1.UPDATE_COURSE,name='update_course'),
    path('admin1/course/delete/<str:id>',admin1.DELETE_COURSE,name='delete_course'),
    path('admin1/staff/send_notification',admin1.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('admin1/staff/save_notification',admin1.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),



# Admin panel(Fuad)
    path('Admin1/Subject/Add', admin1.ADD_SUBJECT, name='add_subject'),
    path('Amin1/Subject/View',admin1.VIEW_SUBJECT,name='view_subject'),
    path('Admin1/Staff/Add', admin1.ADD_STAFF, name='add_staff'),
    path('Admin1/Staff/View', admin1.VIEW_STAFF, name='view_staff'),
    path('Admin1/Staff/Edit/<str:id>', admin1.EDIT_STAFF, name='edit_staff'),
    path('Admin1/Staff/Update', admin1.UPDATE_STAFF, name='update_staff'),
    path('Admin/Staff/Delete/<str:admin>', admin1.DELETE_STAFF, name='delete_staff'),




    path('admin1/student/edit/<str:id>',admin1.EDIT_STUDENT,name='edit_student'),
    path('admin1/student/update',admin1.UPDATE_STUDENT,name='update_student'),

#Student Panel
    path('student/home',student.HOME,name='student_home'),


#staff
    path('staff/home', staff.HOME, name='staff_home'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
