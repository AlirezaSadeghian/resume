from django.shortcuts import render

def index(request):
    contex = {'matn1':'Hello! I am Alireza Sadeghian. Web Design, Python Programmer,  Django and Sales Expert.','matn2':'Programming and art have always been my interests and today I have tried to integrate them in my work by working in the front field. Due to the teamwork spirit I have, I can play an effective role in advancing the teams goals.','matn3':'Darukodeh is a company that sells pharmaceutical, herbal, sports supplements, etc. online, where I am working as a sales and check expert and with all the work steps, including order registration and complete processing. .. I am fully familiar with and have worked with several related software including Rayan Daru (Darusaz) and am familiar with it.'}
    return render(request,'home/index.html',contex)