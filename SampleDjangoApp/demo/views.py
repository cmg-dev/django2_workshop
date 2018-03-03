from django.http import HttpResponse
from django.template import loader

from .models import Reporter

def index(request):
    reporters = Reporter.objects.all()
    template = loader.get_template('reporters/index.html')
    context = {
            'reporters': reporters,
            'has_reporters': len(reporters) > 0,
    }
    return HttpResponse(template.render(context, request))

def test_with_argument(request, greeting):
    return HttpResponse('{}'.format(greeting))

def index_alternative(request):
    from django.shortcuts import render

    reporters = Reporter.objects.all()
    context = {
            'reporters': reporters,
            'has_reporters': len(reporters) > 0,
    }
    return render(request, 'reporters/index.html', context)

def solve(request):
    from django.shortcuts import render

    context = {
            'matrix_rows': range(1,5),
            'matrix_cols': range(1,5),
    }
    return render(request, 'matrix/index.html', context)

def solution(request):
    import solver.s as s

    coeffs = []
    bs = []
    for i in range(1,3):
        for j in range(1,3):
            coeff_name = 'a_{}_{}'.format(i,j)
            coeffs.append(int(request.POST[coeff_name]))

        b_name = 'b_{}'.format(i)
        bs.append(int(request.POST[b_name]))

    A = [[coeffs[0], coeffs[1]],
            [coeffs[2],coeffs[3]]]

    b = [[bs[0]], [bs[1]]]

    return HttpResponse('0 = A({}) - b({}) -> x = {}'.format(A, b, s.solve(A,b)))
