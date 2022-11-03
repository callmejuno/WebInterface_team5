from django.shortcuts import render, redirect
from forthapp.models import Meeting


def c(request) :
    if request.method == 'POST' :
        name = request.POST.get('name')
        personnel = request.POST.get('personnel')
        title = request.POST.get('title')
        meetingdate = request.POST.get('meetingdate')
        meeting = Meeting(name=name,personnel=int(personnel), title=title, meetingdate=meetingdate)
        meeting.save();
        context = { "msg" : "저장 완료되었어용"  }
    else :
        context = None
    return render(request, 'c.html', context)

def r(request, id=0) :
    if id == 0 :
        meetings = Meeting.objects.all()
        context = {"meetings": meetings}
    else :
        try:
            meeting = Meeting.objects.get(id = id)
            context = {"meeting": meeting}
        except Meeting.DoesNotExist:
            context = {"msg": str(id) + '번 데이터가 없어용ㅜ'}
    return render(request, 'r.html', context)

def u(request, id) :
    if request.method == 'POST' :
        meeting = Meeting.objects.get(id=id)
        meeting.name = request.POST.get('name')
        meeting.personnel = request.POST.get('personnel')
        meeting.title = request.POST.get('title')
        meeting.meetingdate = request.POST.get('meetingdate')
        meeting.save();
        context = { "msg" : "수정 완료되었어용"  }
    else :
        meeting = Meeting.objects.get(id=id)
        context = {"meeting": meeting}
    return render(request, 'u.html', context)

def d(request, id) :
    try :
        meeting = Meeting.objects.get(id=id)
        meeting.delete()
        context = {"msg": '삭제 되었어용'}
        #return redirect("R1")
    except Meeting.DoesNotExist :
        context = {"msg": str(id)+'번 데이터가 없어서 삭제하지 못했어용'}
    return render(request, 'd.html', context)


