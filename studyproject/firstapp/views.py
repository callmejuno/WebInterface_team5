from django.http import HttpResponse
def welcome(request):
    return HttpResponse("<h1>장고 공부를 재미있게 합시다</h1>")