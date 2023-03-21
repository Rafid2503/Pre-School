from django.shortcuts import render,redirect
from app.models import Staff,Staff_Notification,Staff_leave,Staff_Feedback,Subject,Session_Year,Student,Attendance,Attendance_Report


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