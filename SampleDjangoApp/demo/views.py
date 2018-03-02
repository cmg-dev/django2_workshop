from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world.")

def test_with_argument(request, greeting):
    return HttpResponse('{}'.format(greeting))
