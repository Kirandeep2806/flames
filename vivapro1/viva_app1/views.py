from django.shortcuts import render
from datetime import datetime
from viva_app1.models import Flames, Contact

# Create your views here.

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        feedback = request.POST.get('feedback')
        contact = Contact(name=name, gender=gender, feedback=feedback)
        contact.save()
    return render(request, 'home.html')

def play(request):
    return render(request, 'play.html')

def contact(request):
    return render(request, 'contact.html')

def result(request):
    if request.method == "POST":
        name1 = request.POST.get('name1')
        name2 = request.POST.get('name2')
        flame = Flames(name1=name1, name2=name2, date=datetime.today())
        flame.save()
        for i in range(len(name1)):
            for j in range(len(name2)):
                if name1[i] == name2[j]:
                    name1 = name1[:i] + "@" + name1[i+1:]
                    name2 = name2[:j] + "@" + name2[j+1:]
                    break
        count = 0
        for i in name1:
            if i != "@":
                count = count + 1
        for i in name2:
            if i != "@":
                count = count + 1
        f = "FLAMES"; ans = ""
        n = 0; i = 0
        while ("F" in f) or ("L" in f) or ("A" in f) or ("M" in f) or ("E" in f) or\
                ("S" in f):
            if f[i] != "@":
                n = n + 1
            if n == count:
                ans = f[i]
                f = f[:i] + "@" + f[i+1:]
                n = 0
            if i == 5:
                i = 0
            else:
                i = i + 1
        if ans == "F":
            ans = "FRIENDS"
        elif ans == "L":
            ans = "LOVE"
        elif ans == "A":
            ans = "AFFECTION"
        elif ans == "M":
            ans = "MARRIAGE"
        elif ans == "E":
            ans = "ENEMIES"
        elif ans == "S":
            ans = "SIBLINGS"
        answers = {"ans": ans}

        return render(request, 'result.html', answers)
