from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
# Create your views here.


@csrf_exempt
def index(request):
    return render(request, 'pages/home.html')


@csrf_exempt
def data(request):
    bad_file = open('/home/truongson/TS/Classification/Review/data/bad/bad.txt', 'r')
    good_file = open('/home/truongson/TS/Classification/Review/data/good/good.txt', 'r')
    normal_file = open('/home/truongson/TS/Classification/Review/data/normal/normal.txt', 'r')
    data = {
        'good': str(sum(1 for i in good_file)),
        'bad': str(sum(1 for i in bad_file)),
        'normal': str(sum(1 for i in normal_file))
    }
    return render(request, 'pages/input.html', data)


@csrf_exempt
def save_data(request):
    if request.GET['select'] != 'Select class' and request.GET['input'] != '':
        bad_file = open('/home/truongson/TS/Classification/Review/data/bad/bad.txt', 'a')
        good_file = open('/home/truongson/TS/Classification/Review/data/good/good.txt', 'a')
        normal_file = open('/home/truongson/TS/Classification/Review/data/normal/normal.txt', 'a')
        if request.GET['select'] == 'good':
            good_file.write(request.GET['input'] + '\n')
            good_file.close()
        elif request.GET['select'] == 'bad':
            bad_file.write(request.GET['input'] + '\n')
            bad_file.close()
        elif request.GET['select'] == 'normal':
            normal_file.write(request.GET['input'] + '\n')
            normal_file.close()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseBadRequest(status=404)


