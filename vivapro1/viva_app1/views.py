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
        n1 = name1; n2 = name2
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

        bgm = ""
        desc = ""
        if ans == "F":
            ans = "FRIENDS"
            bgm = "static/audio/F.mp3"
            desc = "You truly are connected by heart! I'm sure your friendship will cherish more and more"
        elif ans == "L":
            ans = "LOVE"
            bgm = "static/audio/L.mp3"
            desc = "Lucky You!!! Made for each other, huh? I'm sure your 'LOVE' will bloom and blossom!"
        elif ans == "A":
            ans = "AFFECTION"
            bgm = "static/audio/A.mp3"
            desc = "Seems like 'AFFECTION' is the word for your relation! True Affection resides in both of your hearts!"
        elif ans == "M":
            ans = "MARRIAGE"
            bgm = "static/audio/M.mp3"
            desc = "Soulmates, huh? You both are destined to be married, Good Luck!"
        elif ans == "E":
            ans = "ENEMIES"
            bgm = "static/audio/E.mp3"
            desc = "Oh No!!!Apparently, you both may not get along very well...Hope you bury the hatchet!"
        elif ans == "S":
            ans = "SIBLINGS"
            bgm = "static/audio/S.mp3"
            desc = "Side by side or miles apart, you are 'SIBLINGS' connected by heart!"
        answers = {
            "name1": n1,
            "name2": n2,
            "ans": ans,
            "bgm": bgm,
            "desc": desc,
        }
        print(name1, name2)
        flame = Flames(name1=n1, name2=n2, result=ans, date=datetime.today())
        flame.save()
        return render(request, 'result.html', answers)