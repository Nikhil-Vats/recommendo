from django.http import HttpResponse
from django.shortcuts import render, render_to_response, RequestContext
from uno.models import Question_m
from django.views.generic import FormView
from uno.forms import Question_f
import requests
#rom uno.info import information
from copy import deepcopy
from uno.a import info1 as information
#from django.template.defaulttags import register

pro = []
'''
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
'''
def data_handling(budget, profession, gender, location, prefer_to_chinese, majoruse, size):
    print("\n\n\n\n\n\n\n\n",)
    print("here",budget, profession, gender, location, prefer_to_chinese, majoruse, size)
    constant = 1
    global pro
    pro = []
    phones = []
    score = [1, 1, 1, 1, 1, 1, 1, 1]
    for i in range(len(information)):
        if 5000 <= budget <= 8000:
            if 5000 <= information[i][0] <= 7000:
                phones.append(information[i])
        elif 8000 <= budget <= 12000:
            if 8000 <= information[i][0] <= 12000:
                phones.append(information[i])
        elif 12000 <= budget <= 16000:
            if 12000 <= information[i][0] <= 16000:
                phones.append(information[i])
        elif 16000 <= budget <= 25000:
            if 16000 <= information[i][0] <= 25000:
                phones.append(information[i])
        elif 25000 <= budget <= 35000:
            if 25000 <= information[i][0] <= 35000:
                phones.append(information[i])
        elif 35000 <= budget <= 50000:
            if 35000 <= information[i][0] <= 50000:
                phones.append(information[i])
        elif budget >= 50000:
            if information[i][0] >= 50000:
                phones.append(information[i])

    if profession == "student":
        score[2] += constant
        score[3] += constant
        score[4] += constant

    elif profession == "job":
        score[2] += constant
        score[3] += constant
        score[5] += constant

    elif profession == "business":
        score[5] += constant
        score[6] += constant
        score[0] += constant

    elif profession == "retired":
        score[0] += constant
        score[6] += constant

    if gender == "male":
        score[4] += constant

    elif gender == "female":
        score[3] += constant

    if location == "urban":
        score[3] += constant
    elif location == "rural":
        score[0] += constant

    if prefer_to_chinese == "Yes":
        score[0] -= 1

    for i in majoruse:
        if i == 'Photography':
            score[3] += constant
        if i == 'Gaming':
            score[4] += constant
        if i == 'Social Media':
            score[2] += constant
        if i == 'Videos & Movies':
            score[2] += constant
            score[5] += constant

    print(score)
    for j in range(len(phones)):
        for i in range(7):
            phones[j][2][i] *= score[i] ## 0-Price 1-Name 2-Features
        phones[j].append(sum(phones[j][2])) # 3-Pro 4-Con 5-Link 6-Sum

    phones.sort(key=lambda x: x[-1], reverse=True)
    pro = deepcopy(phones[:3])
    del phones
    for i in range(len(pro)):
        print(pro[i])
    return

def index(request):
    context_dict = {'boldmessage': "Unbox"}
    return render(request, 'index.html', context=context_dict)

def question(request):
    return render(request, 'questions.html')

def search(request):
    form = request.GET
    print("\n\nHere\n\n\n")
    print(form)
    majoruse = []
    if "selector2" in form:
        majoruse.append('Videos & Movies')
    if "selector3" in form:
        majoruse.append('Gaming')
    if "selector4" in form:
        majoruse.append('Social Media')
    if "selector5" in form:
        majoruse.append('Photography')
    data_handling(int(form['budget']), form['profession'], form['gender'], form['location'], 0, majoruse, 0)
    return product(request)

def product(request):
    global pro
    context_dict = {'name': pro[0][1], 'price':pro[0][0], 'pro1':pro[0][3][0], 'pro2':pro[0][3][1], 'pro3':pro[0][3][2], 'con':pro[0][4][0], 'link':pro[0][5], 'name2': pro[1][1], 'name3': pro[2][1],
    'pro21':pro[1][3][0], 'pro22':pro[1][3][1], 'pro23':pro[1][3][2], 'con2':pro[1][4][0],
    'pro31':pro[2][3][0], 'pro32':pro[2][3][1], 'pro33':pro[2][3][2], 'con3':pro[2][4][0], 'score':pro[0][-1], 'score2':pro[1][-1], 'score3':pro[2][-1]}
    return render_to_response('product.html', {'dictionary': context_dict}, context_instance=RequestContext(request))

def test(request):
    context_dict = {'bold': "Unbox", 'hello':"hola"}
    return render_to_response('test.html', {'dictionary': context_dict}, context_instance=RequestContext(request))
