from django.shortcuts import render,redirect
from app.models import Staff,Staff_Notification,Staff_leave,Staff_Feedback,Subject,Session_Year,Student,Attendance,Attendance_Report,StudentResult, Student_Notification,Student_Feedback, Student_leave
from django.contrib import messages

def HOME(request):
    return render(request,'students/home.html')


def STUDENT_VIEW_ATTENDANCE(request):

    student=Student.objects.get(admin=request.user.id)
    subjects=Subject.objects.filter(course=student.course_id)

    action=request.GET.get('action')
    get_subject=None
    attendance_report=None


    if action is not None:
        if request.method == "POST":
            subject_id=request.POST.get('subject_id')
            get_subject=Subject.objects.get(id=subject_id)


            attendance_report=Attendance_Report.objects.filter(student_id=student,attendance_id__subject_id=subject_id)

    context={
        'subjects':subjects,
        'action':action,
        'get_subject':get_subject,
        'attendance_report':attendance_report,

    }

    return render(request,'students/view_attendance.html',context)


def STUDENT_VIEW_RESULT(request):

    student=Student.objects.get(admin=request.user.id)
    result=StudentResult.objects.filter(student_id=student)

    mark=None
    for i in result:
        assignment_mark=i.assignment_mark
        exam_mark=i.exam_mark
        mark=assignment_mark+exam_mark

    context={

       'result':result,
        'mark':mark,

    }

    return render(request,'students/view_result.html',context)


def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin= request.user.id)
    for i in student:
        student_id=i.id
        notification =Student_Notification.objects.filter(student_id= student_id)
        context={
            'notification':notification
        }

    return render(request,'students/notification.html',context)


def STAFF_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Student_Notification.objects.get(id = status)
    notification.status=1
    notification.save()

    return redirect('student_notification')


def STUDENT_FEEDBACK(request):
    student_id=Student.objects.get(admin=request.user.id)
    feedback_history= Student_Feedback.objects.filter(student_id=student_id)

    context={
        'feedback_history':feedback_history,

    }
    return render(request, 'students/feedback.html',context)


def STUDENT_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        student = Student.objects.get(admin=request.user.id)
        feedbacks = Student_Feedback(
            student_id =student,
            feedback=feedback,
            feedback_reply ="",
        )
        feedbacks.save()
        return redirect('student_feedback')


def STUDENT_LEAVE(request):
    student =Student.objects.get(admin = request.user.id)
    student_leave_history = Student_leave.objects.filter(student_id =student)
    context={
        'student_leave_history':student_leave_history
    }
    return render(request,'students/apply_leave.html',context)


def STUDENT_LEAVE_SAVE(request):
    if request.method =="POST":
        Leave_date =request.POST.get('Leave_date')
        Leave_message=request.POST.get('Leave_message')

        student_id =Student.objects.get(admin=request.user.id)

        student_leave= Student_leave(
            student_id=student_id,
            data=Leave_date,
            message =Leave_message,
        )
        student_leave.save()
        messages.success(request,'Leave Message Successfully Sent ! ')
        return redirect('student_leave')