from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import List, ListItem
# Create your views here.


def hello(request):
    return HttpResponse('Hello World!')


def search(request):
    spzb = request.GET['spzb']   # 个税清单
    spbh = request.GET['spbh']   # 税票字号
    tfrq = request.GET['tfrq']   # 填发日期
    hjje = request.GET['hjje']  # 合计金额
    pzzl = request.GET['pzzl']
    special = request.GET['special']

    response = spzb + spbh + tfrq + hjje
    '''
    latest_question_list = List.objects.all()
    response = ""
    for item in latest_question_list:
        response += item.taxpayer_idCard_num
    '''
    return HttpResponse(response)


def read_by_pdf(request):
    return render(request, 'taxSite/viewer.html')


def test(request):
    return render(request, 'taxSite/test.html')

