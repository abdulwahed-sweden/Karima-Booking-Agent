from django.shortcuts import render

def index(request):
    # عرض الصفحة الرئيسية
    return render(request, 'index.html')
