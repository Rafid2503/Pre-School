from django.shortcuts import render,redirect
from app.models import Staff,Staff_Notification,Staff_leave
from django.contrib import messages

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


def STAFF_APPLY_LEAVE(request):
    staff=Staff.objects.filter(admin = request.user.id)
    for i in staff:
        staff_id = i.id
        staff_leave_history = Staff_leave.objects.filter(staff_id = staff_id)

        context = {
            'staff_leave_history':staff_leave_history,
        }
    return render(request,'staff/apply_leave.html',context)


def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method =="POST":
        Leave_date=request.POST.get('Leave_date')
        Leave_message =request.POST.get('Leave_message')

        staff=Staff.objects.get(admin=request.user.id)
        leave=Staff_leave(
            staff_id=staff,
            data=Leave_date,
            message=Leave_message,
        )
        leave.save()
        messages.success(request,'Leave Message Successfully Send ! ')
    return redirect('staff_apply_leave')


def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification=Staff_Notification.objects.get(id=status)
    notification.status=1
    notification.save()
    return redirect('staff_notifications')