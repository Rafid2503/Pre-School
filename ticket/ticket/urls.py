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

    path('Admin1/Subject/View',admin1.VIEW_SUBJECT,name='view_subject'),
    path('Admin1/Subject/Edit/<str:id>', admin1.EDIT_SUBJECT, name='edit_subject'),
    path('Admin1/Subject/Update',admin1.UPDATE_SUBJECT,name='update_subject'),
    path('Admin1/Subject/Delete/<str:id>',admin1.DELETE_SUBJECT,name='delete_subject'),

    path('Admin1/Staff/feedback',admin1.STAFF_FEEDBACK, name = 'staff_feedback_reply'),
    path('Admin1/Staff/feedback/save',admin1.STAFF_FEEDBACK_SAVE, name = 'staff_feedback_reply_save'),


#Session
    path('Admin1/Session/Add',admin1.ADD_SESSION,name='add_session'),
    path('Admin1/Session/View',admin1.VIEW_SESSION, name='view_session'),
    path('Admin1/Session/Edit/<str:id>', admin1.EDIT_SESSION, name='edit_session'),
    path('Admin1/Session/Update',admin1.UPDATE_SESSION, name='update_session'),
    path('Admin1/Session/Delete/<str:id>',admin1.DELETE_SESSION,name='delete_session'),

#staff Leave
    path('Staff/Apply_leave',staff.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
    path('Admin1/Staff/Leave_view', admin1.staff_leave_view, name='staff_leave_view'),
    path('Staff/Apply_leave_save',staff.STAFF_APPLY_LEAVE_SAVE,name='staff_apply_leave_save'),
    path('Admin1/Staff/approve_leave/<str:id>',admin1.STAFF_APPROVE_LEAVE,name='staff_approve_leave'),
    path('Admin1/Staff/disapprove_leave/<str:id>',admin1.STAFF_DISAPPROVE_LEAVE,name='staff_disapprove_leave'),



    path('admin1/student/edit/<str:id>',admin1.EDIT_STUDENT,name='edit_student'),
    path('admin1/student/update',admin1.UPDATE_STUDENT,name='update_student'),

#Student Panel
    path('student/home',student.HOME,name='student_home'),


#staff notification
    path('staff/home', staff.HOME, name='staff_home'),
    path('staff/notifications', staff.NOTIFICATIONS, name='staff_notifications'),
    path('staff/mark_as_done/<str:status>', staff.STAFF_NOTIFICATION_MARK_AS_DONE, name='staff_notifications_mark_as_done'),




    path('staff/take_attendance', staff.STAFF_TAKE_ATTENDANCE, name='staff_take_attendance'),
    path('staff/save_attendance', staff.STAFF_SAVE_ATTENDANCE, name='staff_save_attendance'),
    path('staff/view_attendance', staff.STAFF_VIEW_ATTENDANCE, name='staff_view_attendance'),


#Student notification
    path('admin1/student/send_notification', admin1.STUDENT_SEND_NOTIFICATION, name='student_send_notification'),
    path('admin1/student/save_notification', admin1.SAVE_STUDENT_NOTIFICATION, name='save_student_notification'),


#staff feedback
    path('Staff/Feedback',staff.STAFF_FEEDBACK,name= 'staff_feedback'),
    path('Staff/Feedback/Save',staff.STAFF_FEEDBACK_SAVE, name='staff_feedback_save'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
