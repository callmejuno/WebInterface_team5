from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import  JsonResponse
from .models import Visitor, Reply

def v_create(request) :
        name = request.POST['name']
        memo = request.POST['memo']
        vdata = Visitor(name=name, memo=memo)
        vdata.save()
        return redirect("vR")

def v_read(request) :
    page = request.GET.get('page', 1)
    vlist = Visitor.objects.all()
    paginator = Paginator(vlist, 3)
    #print(paginator)
    vlistpage = paginator.get_page(page)
    #print(type(vlistpage))
    #for d in vlistpage :
    #    print(type(d), d)
    context = {"vlist": vlistpage}
    return render(request, 'visitor_crud.html', context)

def v_update(request):
    if request.method == "POST" :
        pk = request.GET.get("pk")
        visitor = Visitor.objects.get(pk=pk)
        visitor.name = request.POST['name']
        visitor.memo = request.POST['memo']
        visitor.save()
        return redirect("vR")
    else :
        pk = request.GET.get("pk")
        visitor = Visitor.objects.get(pk=pk)
        jsonContent = {"name" : visitor.name, "memo": visitor.memo }
        return JsonResponse( jsonContent, json_dumps_params={'ensure_ascii':False})

def v_delete(request) :
    pk = request.GET['pk']
    visitor = Visitor.objects.get(pk=pk)
    visitor.delete()
    return redirect("vR")

def reply_create(request):
    content = request.GET['content']
    pk = request.GET['pk']
    visitor = Visitor.objects.get(pk=pk)  # pk=pk, id=pk
    rdata = Reply(content=content, visitor=visitor)
    rdata.save()
    return JsonResponse({"result":"success"})


def reply_read(request):
    pk = request.GET['pk']
    rlist = []
    reply = Reply.objects.filter(visitor=pk)
    for r in reply :
        print(r)
        rlist.append(r.content)
    if len(rlist) == 0 :
        rlist = ['힝~ 아직 소중한 댓글이 없어용']
    return JsonResponse({"result": rlist})

def search1(request, name) :
    page = request.GET.get('page', 1)
    vlist = Visitor.objects.filter(name = name)
    paginator = Paginator(vlist, 3)
    vlistpage = paginator.get_page(page)
    context = {"vlist": vlistpage}
    return render(request, 'visitor_crud.html', context)

def search2(request, content):
    page = request.GET.get('page', 1)
    vlist = Visitor.objects.filter(memo__contains=content)
    paginator = Paginator(vlist, 3)
    vlistpage = paginator.get_page(page)
    context = {"vlist": vlistpage}
    return render(request, 'visitor_crud.html', context)

