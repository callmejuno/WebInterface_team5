from django.shortcuts import render
from .models import Upload


def fileupload(request) :
    context = None
    if request.method == 'POST' :
        upload = Upload(title = request.POST['title'], content=request.POST['content'], photo=request.FILES['photo'])
        upload.save()
        context = {"upload" : upload}

    return render(request, "fileupload.html", context)

def fileuploadmulti(request) :
    context = None
    uploadlist = []
    if request.method == 'POST' :
        photolist = request.FILES.getlist("multiphoto")
        for num, data in enumerate(photolist) :
            upload = Upload(title=f"title{num}", content=f"content{num}", photo=data)
            upload.save()
            uploadlist.append(upload)
        context = {"uploadlist" : uploadlist}

    return render(request, "fileuploadmulti.html", context)
