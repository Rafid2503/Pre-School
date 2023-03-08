from django.shortcuts import render,redirect
from app.models import Staff,Staff_Notification

def HOME(request):
    return render(request,'staff/home.html')


def NOTIFICATIONS(request):
    staff=Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id=i.id
        notification=Staff_Notification.objects.filter(staff_id=staff_id)

        context={

            'notification':notification,

        }
        return render(request,'staff/notification.html',context)