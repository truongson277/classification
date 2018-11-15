from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseBadRequest, JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .static.data.predict import main
import os
from keras import backend as K
K.clear_session()
os.environ['TF_CPP_MIN_LOG_LEVEL'] ='2'


DIR_DATA = 'Review/static/data/'


@csrf_exempt
def index(request):
    return render(request, 'pages/home.html')


@csrf_exempt
def data(request):
    bad_file = open(DIR_DATA + 'bad/bad.txt', 'r')
    good_file = open(DIR_DATA + 'good/good.txt', 'r')
    normal_file = open(DIR_DATA + 'normal/normal.txt', 'r')
    data = {
        'good': str(sum(1 for i in good_file)),
        'bad': str(sum(1 for i in bad_file)),
        'normal': str(sum(1 for i in normal_file))
    }
    return render(request, 'pages/input.html', data)


@csrf_exempt
def save_data(request):
    if request.GET['select'] != 'Select class' and request.GET['input'] != '':
        bad_file = open(DIR_DATA + 'bad/bad.txt', 'a')
        good_file = open(DIR_DATA + 'good/good.txt', 'a')
        normal_file = open(DIR_DATA + 'normal/normal.txt', 'a')
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


@csrf_exempt
def predict_review(request):
    return render(request, 'pages/predict.html')


@csrf_exempt
def save_predict(request):
    if request.GET['inputPredict'] != '':
        K.clear_session()
        target = open(DIR_DATA + 'target.txt', 'a')
        target.write(request.GET['inputPredict'].replace(".", "\n", 10000) + '\n')
        target.close()
        results = main()
        return JsonResponse(results)
    else:
        return HttpResponseBadRequest(status=404)


@csrf_exempt
def save_good(request):
    for i in range(0, int(request.GET['index'])):
        print(request.GET[str(i)])
    return HttpResponse(status=200)
