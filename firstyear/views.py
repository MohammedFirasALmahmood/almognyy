from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import AE1
from .models import AE4
from .models import AE4M
from .models import AEG
from .models import AEGM
from .models import AEP
from .models import AEPS
from .models import AGMAGolden as AGMAG
from .models import AGMAGoldenM as AGMAGM
from .models import AGMAPriveos as AGMAP
from .models import AGMAPriveosS as AGMAPS
from .models import AGrammar4M as AG4M
from .models import AGrammer1 as AG1
from .models import AGrammer4 as AG4
from .models import AMorphology1 as AM1
from .models import AMorphology4 as AM4
from .models import AMorphology4M as AM4M
from .models import APre_IslamicLiterature as APre
from .models import AResearchSeeds1 as ARS1
from .models import AResearchSeeds4 as ARS4
from .models import AResearchSeeds4M as ARS4M
from .models import AResearchSeedsG as ARSG
from .models import AResearchSeedsGM as ARSGM
from .models import AResearchSeedsP as ARSP
from .models import AResearchSeedsPS as ARSPS
from .models import ATH1
from .models import ATH4
from .models import ATH4M
from .models import ATHG
from .models import ATHGM
from .models import ATHP
from .models import ATHPS
from .models import Application1 as AP1
from .models import Application2 as AP2
from .models import Application3 as AP3
from .models import Application4 as AP4
from .models import Application5 as AP5
from .models import ApplicationEx1 as APEx1
from .models import ApplicationEx2 as APEx2
from .models import ApplicationEx3 as APEx3
from .models import ApplicationEx4 as APEx4
from .models import ApplicationEx5 as APEx5
from .models import ApplicationEx6 as APEx6
from .models import ApplicationExM as APExM
from .models import HPre_IslamicLiterature as HPre
from .models import PPre_IslamicLiterature as PPre
from .models import Users
from .models import WGMAGlden as WGMAG
from .models import WGMAPriveos as WGMAP
from .models import WGrammar as WG
from .models import WMorphology as WM
from .models import WResearchSeedsG as WRSG
from .models import WResearchSeedsL as WRSL
from .models import WResearchSeedsP as WRSP
from .models import WTStatement as WTS
from .models import WPStatement as WPS
from .models import WGStatement as WGS
from .models import WPPStatement as WPPS
from .models import APStatement1 as APS1
from .models import APStatement4 as APS4
from .models import APStatement4M as APS4M
from .models import ATStatement1 as ATS1
from .models import ATStatement4 as ATS4
from .models import ATStatement4M as ATS4M


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST.get('Name')
        password = request.POST.get('password')
        reg = Users(username=username, password=password)
        reg.save()
    return render(request, 'firstyear/register.html')


def login(request):
    if request.method == 'POST':
        username = str(request.POST.get('username'))
        password = request.POST.get('password')
        if Users.objects.get(username=username).id == Users.objects.get(password=password).id:
            print(True)
            return redirect('/firstyear/main/')
        else:
            return HttpResponse(username)

    return render(request, 'firstyear/login.html')


def main(request):
    return render(request, 'firstyear/main.html')


def firstsemester(request):
    return render(request, 'firstyear/firstsemester.html')


def GMA(request):
    return render(request, 'firstyear/GMA/GMA.html')


def WGMA(request):
    return render(request, 'firstyear/GMA/WGMA.html')


def AGMA(request):
    return render(request, 'firstyear/GMA/AGMA.html')


# def
class Form1(forms.Form):
    file = forms.FileField()


def WGrammarM(request):
    list = WG.objects.all()
    return render(request, 'firstyear/GMA/WGrammerM.html', {'name': list})


def WGrammerE(request, number):
    list = WG.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('WGrammarM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('WGrammarM')
    return render(request, 'firstyear/GMA/WGrammerE.html', {'name': list})


def WGrammar(request):
    list = WG.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = WG.objects.create(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                                          publish=publish)
                Cdate.save()
                return redirect(WGrammarM)

    return render(request, 'firstyear/GMA/WGrammar.html', {'names': list, 'form': file})


def WMorphologyM(request):
    list = WM.objects.all()
    return render(request, 'firstyear/GMA/WMorphologyM.html', {'name': list})


def WMorphologyE(request, number):
    list = WM.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('WMorphologyM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('WMorphologyM')
    return render(request, 'firstyear/GMA/WMorphologyE.html', {'name': list})


def WMorphology(request):
    list = WM.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = WM(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                           publish=publish)
                Cdate.save()
                return redirect('WMorphologyM')

    return render(request, 'firstyear/GMA/WMorphology.html', {'names': list, 'form': file})


def WGMAPriveosM(request):
    list = WGMAP.objects.all()
    return render(request, 'firstyear/GMA/WGMAPriveosM.html', {'name': list})


def WGMAPriveosE(request, pyear, number):
    list = WGMAP.objects.get(pyear=pyear, number=number)
    print(list)
    if 'add' in request.POST:
        pyear = request.POST.get('pyear')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.pyear = pyear
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('WGMAPriveosM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('WGMAPriveosM')
    return render(request, 'firstyear/GMA/WGMAPriveosE.html', {'name': list})


def WGMAPriveos(request):
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                pyear = request.POST.get('pyear')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = WGMAP(pyear=pyear, lfile=request.FILES['file'], lprice=price, number=number, publish=publish)
                Cdate.save()
                return redirect('WGMAPriveosM')

    return render(request, 'firstyear/GMA/WGMAPriveos.html', {'form': file})


def WGMAGoldenM(request):
    list = WGMAG.objects.first()
    return render(request, 'firstyear/GMA/WGMAGoldenM.html', {'name': list})


def WGMAGlden(request):
    list = WGMAG.objects.first()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                publish = bool(request.POST.get('check'))
                Cdate = WGMAG(lname=name, lfile=request.FILES['file'], lprice=price, publish=publish)
                Cdate.save()
                return redirect('WGMAGoldenM')
    return render(request, 'firstyear/GMA/WGMAGlden.html', {'names': list, 'form': file})


def WGMAGoldenE(request):
    list = WGMAG.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('WGMAGoldenM')

    if 'delete' in request.POST:
        member = WGMAG.objects.all()
        member.delete()
        return redirect('WGMAGoldenM')

    return render(request, 'firstyear/GMA/WGMAGoldenE.html', {'name': list})


def AGrammer(request):
    return render(request, 'firstyear/GMA/AGrammar.html', )


def AGrammar1M(request):
    list = AG1.objects.all()

    return render(request, 'firstyear/GMA/AGrammar1M.html', {'name': list})


def AGrammer1(request):
    list = AG1.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AG1(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AGrammar1M')

    return render(request, 'firstyear/GMA/AGrammar1.html', {'names': list, 'form': file})


def AGrammar1E(request, number):
    list = AG1.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('AGrammar1M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AGrammar1M')

    return render(request, 'firstyear/GMA/AGrammar1E.html', {'name': list})


def AGrammar4M(request):
    list = AG4M.objects.all()

    return render(request, 'firstyear/GMA/AGrammar4M.html', {'names': list})


def AGrammar4E(request, number):
    list = AG4M.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('AGrammar4M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AGrammar4M')

    return render(request, 'firstyear/GMA/AGrammar4E.html', {'name': list})


def AGrammar4Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AG4M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AGrammar4M')
    return render(request, 'firstyear/GMA/AGrammar4Add.html')


def AGrammar4(request, number):
    db = AG4M.objects.get(number=number)
    list = AG4.objects.filter(ExNo=db)
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = AG4(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AG4.objects.get(number=number, ExNo=db)
            instance = AG4.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'firstyear/GMA/AGrammar4.html', {'names': list})


def AMorphology(request):
    return render(request, 'firstyear/GMA/AMorphology.html')


def AMorphology1M(request):
    list = AM1.objects.all()

    return render(request, 'firstyear/GMA/AMorphology1M.html', {'name': list})


def AMorphology1(request):
    list = AM1.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AM1(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AMorphology1M')

    return render(request, 'firstyear/GMA/AMorphology1.html', {'names': list, 'form': file})


def AMorphology1E(request, number):
    list = AM1.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('AMorphology1M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AMorphology1M')

    return render(request, 'firstyear/GMA/AMorphology1E.html', {'name': list})


def AMorphology4M(request):
    list = AM4M.objects.all()

    return render(request, 'firstyear/GMA/AMorphology4M.html', {'names': list})


def AMorphology4E(request, number):
    list = AM4M.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('AMorphology4M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AMorphology4M')

    return render(request, 'firstyear/GMA/AMorphology4E.html', {'name': list})


def AMorphology4Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AM4M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AMorphology4M')
    return render(request, 'firstyear/GMA/AMorphology4Add.html')


def AMorphology4(request, number):
    db = AM4M.objects.get(number=number)
    list = AM4.objects.filter(ExNo=db)
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = AM4(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AM4.objects.get(number=number, ExNo=db)
            instance = AM4.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'firstyear/GMA/AMorphology4.html', {'names': list})


def AGMAGoldenM(request):
    list = AGMAGM.objects.first()

    return render(request, 'firstyear/GMA/AGMAGoldenM.html', {'names': list})


def AGMAGoldenE(request):
    list = AGMAGM.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.lprice = price
        list.publish = publish
        list.save()
        return redirect('AGMAGoldenM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AGMAGoldenM')

    return render(request, 'firstyear/GMA/AGMAGoldenE.html', {'name': list})


def AGMAGoldenAdd(request):
    if request.method == "POST":
        name = request.POST.get("name")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AGMAGM(name=name, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AGMAGoldenM')
    return render(request, 'firstyear/GMA/AGMAGoldenAdd.html')


def AGMAGolden(request):
    db = AGMAGM.objects.first()
    list = AGMAG.objects.all()
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')

            Cdate = AGMAG(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                          number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AGMAG.objects.get(number=number)
            instance = AGMAG.objects.get(number=number)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/GMA/AGMAGolden.html', {'names': list})


def AGMAPriveosS(request):
    list = AGMAPS.objects.all()
    return render(request, 'firstyear/GMA/AGMAPriveosS.html', {'name': list})


def AGMAPriveosAdd(request):
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            Cdate = AGMAPS(ExNo=ExNo, semestery=semestery, publish=publish, lprice=lprice)
            Cdate.save()
            return redirect('AGMAPriveosS')

    return render(request, 'firstyear/GMA/AGMAPriveosAdd.html')


def AGMAPriveosM(request, ExNo, semestery):
    list = AGMAPS.objects.get(ExNo=ExNo, semestery=semestery)
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            list.ExNo = ExNo
            list.semestery = semestery
            list.lprice = lprice
            list.publish = publish
            list.save()
        if 'delete' in request.POST:
            list.delete()
            return redirect('AGMAPriveosS')

    return render(request, 'firstyear/GMA/AGMAPriveosM.html', {'name': list})


def AGMAPriveos(request, ExNo, semestery):
    PreviosS = AGMAPS.objects.get(ExNo=ExNo, semestery=semestery)
    list = AGMAP.objects.filter(PreviosS=PreviosS)
    if request.method == "POST":
        if 'add' in request.POST:

            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = AGMAP(PreviosS=PreviosS, question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why,
                          No_true=No_true, number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AGMAP.objects.get(number=number, PreviosS=PreviosS)
            instance = AGMAP.objects.filter(number=number, PreviosS=PreviosS)
            instance.delete()
            member.delete()

    return render(request, 'firstyear/GMA/AGMAPriveos.html', {'names': list})


def Application1(request):
    list = AP1.objects.first()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                publish = bool(request.POST.get('check'))
                Cdate = AP1(lname=name, lfile=request.FILES['file'], lprice=price, publish=publish)
                Cdate.save()
                return redirect('Application1')

        elif 'delete' in request.POST:
            list = AP1.objects.first()
            list.delete()
            return redirect('Application1')

        elif 'edit' in request.POST:
            name = request.POST.get('name')
            price = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            list.lname = name
            list.publish = publish
            list.lprice = price
            list.save()
            return redirect('Application1')

    return render(request, 'firstyear/GMA/Application1.html', {'names': list, 'form': file})


def Application2(request):
    list = AP2.objects.first()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                publish = bool(request.POST.get('check'))
                Cdate = AP2(lname=name, lfile=request.FILES['file'], lprice=price, publish=publish)
                Cdate.save()
                return redirect('Application2')

        elif 'delete' in request.POST:
            list = AP2.objects.first()
            list.delete()
            return redirect('Application2')

        elif 'edit' in request.POST:
            name = request.POST.get('name')
            price = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            list.lname = name
            list.publish = publish
            list.lprice = price
            list.save()
            return redirect('Application2')

    return render(request, 'firstyear/GMA/Application2.html', {'names': list, 'form': file})


def Application(request):
    return render(request, 'firstyear/GMA/Application.html')


def Application3(request):
    list = AP3.objects.first()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                publish = bool(request.POST.get('check'))
                Cdate = AP3(lname=name, lfile=request.FILES['file'], lprice=price, publish=publish)
                Cdate.save()
                return redirect('Application3')

        elif 'delete' in request.POST:
            list = AP3.objects.first()
            list.delete()
            return redirect('Application3')

        elif 'edit' in request.POST:
            name = request.POST.get('name')
            price = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            list.lname = name
            list.publish = publish
            list.lprice = price
            list.save()
            return redirect('Application3')

    return render(request, 'firstyear/GMA/Application3.html', {'names': list, 'form': file})


def Application4(request):
    list = AP4.objects.first()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                publish = bool(request.POST.get('check'))
                Cdate = AP4(lname=name, lfile=request.FILES['file'], lprice=price, publish=publish)
                Cdate.save()
                return redirect('Application4')

        elif 'delete' in request.POST:
            list = AP4.objects.first()
            list.delete()
            return redirect('Application4')

        elif 'edit' in request.POST:
            name = request.POST.get('name')
            price = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            list.lname = name
            list.publish = publish
            list.lprice = price
            list.save()
            return redirect('Application4')

    return render(request, 'firstyear/GMA/Application4.html', {'names': list, 'form': file})


def Application5(request):
    list = AP5.objects.first()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                publish = bool(request.POST.get('check'))
                Cdate = AP5(lname=name, lfile=request.FILES['file'], lprice=price, publish=publish)
                Cdate.save()
                return redirect('Application5')

        elif 'delete' in request.POST:
            list = AP5.objects.first()
            list.delete()
            return redirect('Application5')

        elif 'edit' in request.POST:
            name = request.POST.get('name')
            price = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            list.lname = name
            list.publish = publish
            list.lprice = price
            list.save()
            return redirect('Application5')

    return render(request, 'firstyear/GMA/Application5.html', {'names': list, 'form': file})


def ApplicationExM(request, id):
    db = APExM.objects.get(id=id)

    if request.method == "POST":
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        print(price)
        print(publish)
        db.lprice = price
        db.publish = publish
        db.save()
        return redirect('ApplicationEx')
    return render(request, "firstyear/GMA/ApplicationExM.html", {'names': db})


def ApplicationEx(request):
    list1 = APExM.objects.get(id=1)
    list2 = APExM.objects.get(id=2)
    list3 = APExM.objects.get(id=3)
    list4 = APExM.objects.get(id=4)
    list5 = APExM.objects.get(id=5)
    list6 = APExM.objects.get(id=6)
    return render(request, 'firstyear/GMA/ApplicationEx.html',
                  {'names1': list1, 'names2': list2, 'names3': list3, 'names4': list4, 'names5': list5,
                   'names6': list6})


def ApplicationEx1(request):
    db = APExM.objects.get(id=1)
    list = APEx1.objects.all()
    if request.method == "POST":
        if 'add' in request.POST:

            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')

            Cdate = APEx1(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                          number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            id = request.POST.get('number')
            member = APEx1.objects.get(number=id)
            instance = APEx1.objects.filter(number=id)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/GMA/ApplicationEx1.html', {'names': list})


def ApplicationEx2(request):
    db = APExM.objects.get(id=2)
    list = APEx2.objects.all()
    if request.method == "POST":
        if 'add' in request.POST:

            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')

            Cdate = APEx2(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                          number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            id = request.POST.get('number')
            member = APEx2.objects.get(number=id)
            instance = APEx2.objects.filter(number=id)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/GMA/ApplicationEx2.html', {'names': list})


def ApplicationEx3(request):
    db = APExM.objects.get(id=3)

    list = APEx3.objects.all()
    if request.method == "POST":
        if 'add' in request.POST:

            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            price = request.POST.get('price')
            publish = bool(request.POST.get('check'))

            Cdate = APEx3(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                          number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            id = request.POST.get('number')
            member = APEx3.objects.get(number=id)
            instance = APEx3.objects.filter(number=id)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/GMA/ApplicationEx3.html', {'names': list})


def ApplicationEx4(request):
    db = APExM.objects.get(id=4)

    list = APEx4.objects.all()
    if request.method == "POST":
        if 'add' in request.POST:

            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            price = request.POST.get('price')
            publish = bool(request.POST.get('check'))

            Cdate = APEx4(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                          number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            id = request.POST.get('number')
            member = APEx4.objects.get(number=id)
            instance = APEx4.objects.filter(number=id)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/GMA/ApplicationEx4.html', {'names': list})


def ApplicationEx5(request):
    db = APExM.objects.get(id=5)

    list = APEx5.objects.all()
    if request.method == "POST":
        if 'add' in request.POST:

            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            price = request.POST.get('price')
            publish = bool(request.POST.get('check'))

            Cdate = APEx5(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                          number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            id = request.POST.get('number')
            member = APEx5.objects.get(number=id)
            instance = APEx5.objects.filter(number=id)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/GMA/ApplicationEx5.html', {'names': list})


def ApplicationEx6(request):
    db = APExM.objects.get(id=6)
    list = APEx6.objects.all()
    if request.method == "POST":
        if 'add' in request.POST:

            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            price = request.POST.get('price')
            publish = bool(request.POST.get('check'))

            Cdate = APEx6(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                          number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            id = request.POST.get('number')
            member = APEx6.objects.get(number=id)
            instance = APEx6.objects.filter(number=id)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/GMA/ApplicationEx6.html', {'names': list})


def ResearchSeeds(request):
    return render(request, 'firstyear/ResearchSeeds/ResearchSeeds.html')


def WResearchSeeds(request):
    return render(request, 'firstyear/ResearchSeeds/WResearchSeeds.html')


def WResearchSeedsL(request):
    list = WRSL.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))

                Cdate = WRSL(lname=name, lfile=request.FILES['file'], lprice=price, number=number, publish=publish)
                Cdate.save()

        elif 'delete' in request.POST:
            id = request.POST.get('id')
            member = WRSL.objects.get(id=id)
            instance = WRSL.objects.filter(id=id)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/ResearchSeeds/WResearchSeedsL.html', {'names': list, 'form': file})


def WResearchSeedsG(request):
    list = WRSG.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))

                Cdate = WRSG(lname=name, lfile=request.FILES['file'], lprice=price, number=number, publish=publish)
                Cdate.save()

        elif 'delete' in request.POST:
            id = request.POST.get('id')
            member = WRSG.objects.get(id=id)
            instance = WRSG.objects.filter(id=id)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/ResearchSeeds/WResearchSeedsG.html', {'names': list, 'form': file})


def WResearchSeedsP(request):
    list = WRSP.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))

                Cdate = WRSP(lname=name, lfile=request.FILES['file'], lprice=price, number=number, publish=publish)
                Cdate.save()

        elif 'delete' in request.POST:
            id = request.POST.get('id')
            member = WRSP.objects.get(id=id)
            instance = WRSP.objects.filter(id=id)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/ResearchSeeds/WResearchSeedsP.html', {'names': list, 'form': file})


def AResearchSeeds(request):
    return render(request, 'firstyear/ResearchSeeds/AResearchSeeds.html')


def AResearchSeeds1M(request):
    list = ARS1.objects.all()

    return render(request, 'firstyear/ResearchSeeds/AResearchSeeds1M.html', {'name': list})


def AResearchSeeds1(request):
    list = ARS1.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = ARS1(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                             publish=publish)
                Cdate.save()
                return redirect('AResearchSeeds1M')

    return render(request, 'firstyear/ResearchSeeds/AResearchSeeds1.html', {'names': list, 'form': file})


def AResearchSeeds1E(request, number):
    list = ARS1.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('AResearchSeeds1M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AResearchSeeds1M')

    return render(request, 'firstyear/ResearchSeeds/AResearchSeeds1E.html', {'name': list})


def AResearchSeeds4M(request):
    list = ARS4M.objects.all()

    return render(request, 'firstyear/ResearchSeeds/AResearchSeeds4M.html', {'names': list})


def AResearchSeeds4E(request, number):
    list = ARS4M.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('AResearchSeeds4M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AResearchSeeds4M')

    return render(request, 'firstyear/ResearchSeeds/AResearchSeeds4E.html', {'name': list})


def AResearchSeeds4Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = ARS4M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AResearchSeeds4M')
    return render(request, 'firstyear/ResearchSeeds/AResearchSeeds4Add.html')


def AResearchSeeds4(request, number):
    db = ARS4M.objects.get(number=number)
    list = ARS4.objects.filter(ExNo=db)
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = ARS4(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                         ExNo=db,
                         number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AM4.objects.get(number=number, ExNo=db)
            instance = AM4.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'firstyear/ResearchSeeds/AResearchSeeds4.html', {'names': list})


def AResearchSeedsGM(request):
    list = ARSGM.objects.first()

    return render(request, 'firstyear/ResearchSeeds/AResearchSeedsGM.html', {'names': list})


def AResearchSeedsGE(request):
    list = ARSGM.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.lprice = price
        list.publish = publish
        list.save()
        return redirect('AResearchSeedsGM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AResearchSeedsGM')

    return render(request, 'firstyear/ResearchSeeds/AResearchSeedsGE.html', {'name': list})


def AResearchSeedsGAdd(request):
    if request.method == "POST":
        name = request.POST.get("name")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = ARSGM(name=name, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AResearchSeedsGM')
    return render(request, 'firstyear/ResearchSeeds/AResearchSeedsGAdd.html')


def AResearchSeedsG(request):
    db = ARSGM.objects.first()
    list = ARSG.objects.all()
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')

            Cdate = ARSG(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                         number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = ARSG.objects.get(number=number)
            instance = ARSG.objects.get(number=number)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/ResearchSeeds/AResearchSeedsG.html', {'names': list})


def AResearchSeedsPS(request):
    list = ARSPS.objects.all()
    return render(request, 'firstyear/ResearchSeeds/AResearchSeedsPS.html', {'name': list})


def AResearchSeedsPAdd(request):
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            Cdate = ARSPS(ExNo=ExNo, semestery=semestery, publish=publish, lprice=lprice)
            Cdate.save()
            return redirect('AResearchSeedsPS')

    return render(request, 'firstyear/ResearchSeeds/AResearchSeedsPAdd.html')


def AResearchSeedsPM(request, ExNo, semestery):
    list = ARSPS.objects.get(ExNo=ExNo, semestery=semestery)
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            list.ExNo = ExNo
            list.semestery = semestery
            list.lprice = lprice
            list.publish = publish
            list.save()
        if 'delete' in request.POST:
            list.delete()
            return redirect('AResearchSeedsPS')

    return render(request, 'firstyear/ResearchSeeds/AResearchSeedsPM.html', {'name': list})


def AResearchSeedsP(request, ExNo, semestery):
    PreviosS = ARSPS.objects.get(ExNo=ExNo, semestery=semestery)
    list = ARSP.objects.filter(PreviosS=PreviosS)
    if request.method == "POST":
        if 'add' in request.POST:

            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = ARSP(PreviosS=PreviosS, question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why,
                         No_true=No_true, number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = ARSP.objects.get(number=number, PreviosS=PreviosS)
            instance = ARSP.objects.filter(number=number, PreviosS=PreviosS)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/ResearchSeeds/AResearchSeedsP.html', {'names': list})


def Pre_IslamicLiterature(request):
    return render(request, 'firstyear/Pre_IslamicLiterature/Pre_IslamicLiterature.html', )


def HPre_IslamicLiteratureM(request):
    list = HPre.objects.all()
    return render(request, 'firstyear/Pre_IslamicLiterature/HPre_IslamicLiteratureM.html', {'name': list})


def HPre_IslamicLiteratureE(request, number):
    list = HPre.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('HPre_IslamicLiteratureM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('HPre_IslamicLiteratureM')
    return render(request, 'firstyear/Pre_IslamicLiterature/HPre_IslamicLiteratureE.html', {'name': list})


def HPre_IslamicLiterature(request):
    list = HPre.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = HPre.objects.create(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                                            publish=publish)
                Cdate.save()
                return redirect("HPre_IslamicLiteratureM")

    return render(request, 'firstyear/Pre_IslamicLiterature/HPre_IslamicLiterature.html', {'names': list, 'form': file})


def APre_IslamicLiteratureM(request):
    list = APre.objects.all()
    return render(request, 'firstyear/Pre_IslamicLiterature/APre_IslamicLiteratureM.html', {'name': list})


def APre_IslamicLiteratureE(request, number):
    list = APre.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('APre_IslamicLiteratureM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('APre_IslamicLiteratureM')
    return render(request, 'firstyear/Pre_IslamicLiterature/APre_IslamicLiteratureE.html', {'name': list})


def APre_IslamicLiterature(request):
    list = APre.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = APre.objects.create(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                                            publish=publish)
                Cdate.save()
                return redirect('APre_IslamicLiteratureM')

    return render(request, 'firstyear/Pre_IslamicLiterature/APre_IslamicLiterature.html', {'names': list, 'form': file})




def PPre_IslamicLiteratureM(request):
    list = PPre.objects.all()
    return render(request, 'firstyear/Pre_IslamicLiterature/PPre_IslamicLiteratureM.html', {'name': list})


def PPre_IslamicLiteratureE(request, pyear, number):
    list = PPre.objects.get(pyear=pyear, number=number)
    print(list)
    if 'add' in request.POST:
        pyear = request.POST.get('pyear')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.pyear = pyear
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('PPre_IslamicLiteratureM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('PPre_IslamicLiteratureM')
    return render(request, 'firstyear/Pre_IslamicLiterature/PPre_IslamicLiteratureM.html', {'name': list})


def PPre_IslamicLiterature(request):
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                pyear = request.POST.get('pyear')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = PPre(pyear=pyear, lfile=request.FILES['file'], lprice=price, number=number, publish=publish)
                Cdate.save()
                return redirect('PPre_IslamicLiteratureM')

    return render(request, 'firstyear/Pre_IslamicLiterature/PPre_IslamicLiterature.html', {'form': file})















def AEn(request):
    return render(request, 'firstyear/E/ATh.html')


def AEn1M(request):
    list = AE1.objects.all()

    return render(request, 'firstyear/E/AEn1M.html', {'name': list})


def AEn1(request):
    list = AE1.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AE1(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AEn1M')

    return render(request, 'firstyear/E/ATh1.html', {'names': list, 'form': file})


def AEn1E(request, number):
    list = AE1.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('AEn1M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AEn1M')

    return render(request, 'firstyear/E/AEn1E.html', {'name': list})


def AEn4M(request):
    list = AE4M.objects.all()

    return render(request, 'firstyear/E/AEn4M.html', {'names': list})


def AEn4E(request, number):
    list = AE4M.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('AEn4M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AEn4M')

    return render(request, 'firstyear/E/AEn4E.html', {'name': list})


def AEn4Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AE4M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AEn4M')
    return render(request, 'firstyear/E/AEn4Add.html')


def AEn4(request, number):
    db = AE4M.objects.get(number=number)
    list = AE4.objects.filter(ExNo=db)
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = AE4(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AE4.objects.get(number=number, ExNo=db)
            instance = AE4.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'firstyear/E/AEn4.html', {'names': list})


def AEnGM(request):
    list = AEGM.objects.first()

    return render(request, 'firstyear/E/AEnGM.html', {'names': list})


def AEnGE(request):
    list = AEGM.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.lprice = price
        list.publish = publish
        list.save()
        return redirect('AEnGM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AEnGM')

    return render(request, 'firstyear/E/AEnGE.html', {'name': list})


def AEnGAdd(request):
    if request.method == "POST":
        name = request.POST.get("name")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AEGM(name=name, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AEnGM')
    return render(request, 'firstyear/E/AEnGAdd.html')


def AEnG(request):
    db = AEGM.objects.first()
    list = AEG.objects.all()
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')

            Cdate = AEG(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AEG.objects.get(number=number)
            instance = AEG.objects.get(number=number)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/E/AEnG.html', {'names': list})


def AEnPS(request):
    list = AEPS.objects.all()
    return render(request, 'firstyear/E/AEnPS.html', {'name': list})


def AEnPAdd(request):
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            Cdate = AEPS(ExNo=ExNo, semestery=semestery, publish=publish, lprice=lprice)
            Cdate.save()
            return redirect('AEnPS')

    return render(request, 'firstyear/E/AEnPAdd.html')


def AEnPM(request, ExNo, semestery):
    list = AEPS.objects.get(ExNo=ExNo, semestery=semestery)
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            list.ExNo = ExNo
            list.semestery = semestery
            list.lprice = lprice
            list.publish = publish
            list.save()
        if 'delete' in request.POST:
            list.delete()
            return redirect('AEnPS')

    return render(request, 'firstyear/E/AEnPM.html', {'name': list})


def AEnP(request, ExNo, semestery):
    PreviosS = AEPS.objects.get(ExNo=ExNo, semestery=semestery)
    list = AEP.objects.filter(PreviosS=PreviosS)
    if request.method == "POST":
        if 'add' in request.POST:

            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = AEP(PreviosS=PreviosS, question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why,
                        No_true=No_true, number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AEP.objects.get(number=number, PreviosS=PreviosS)
            instance = AEP.objects.filter(number=number, PreviosS=PreviosS)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/E/AEnP.html', {'names': list})


def ATh(request):
    return render(request, 'firstyear/TH/ATh.html')


def ATh1M(request):
    list = ATH1.objects.all()

    return render(request, 'firstyear/TH/ATh1M.html', {'name': list})


def ATh1(request):
    list = ATH1.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = ATH1(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                             publish=publish)
                Cdate.save()
                return redirect('ATh1M')

    return render(request, 'firstyear/TH/ATh1.html', {'names': list, 'form': file})


def ATh1E(request, number):
    list = ATH1.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        number = request.POST.get("number")
        list.number = number
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('ATh1M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('ATh1M')

    return render(request, 'firstyear/TH/ATh1E.html', {'name': list})


def ATh4M(request):
    list = ATH4M.objects.all()

    return render(request, 'firstyear/TH/ATh4M.html', {'names': list})


def ATh4E(request, number):
    list = ATH4M.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('ATh4M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('ATh4M')

    return render(request, 'firstyear/TH/ATh4E.html', {'name': list})


def ATh4Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = ATH4M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('ATh4M')
    return render(request, 'firstyear/TH/ATh4Add.html')


def ATh4(request, number):
    db = ATH4M.objects.get(number=number)
    list = ATH4.objects.filter(ExNo=db)
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = ATH4(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                         ExNo=db,
                         number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = ATH4.objects.get(number=number, ExNo=db)
            instance = ATH4.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'firstyear/TH/ATh4.html', {'names': list})


def AThGM(request):
    list = ATHGM.objects.first()

    return render(request, 'firstyear/TH/AThGM.html', {'names': list})


def AThGE(request):
    list = ATHGM.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.lprice = price
        list.publish = publish
        list.save()
        return redirect('AThGM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AThGM')

    return render(request, 'firstyear/TH/AThGE.html', {'name': list})


def AThGAdd(request):
    if request.method == "POST":
        name = request.POST.get("name")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = ATHGM(name=name, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AThGM')
    return render(request, 'firstyear/TH/AThGAdd.html')


def AThG(request):
    db = ATHGM.objects.first()
    list = ATHG.objects.all()
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')

            Cdate = ATHG(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                         number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = ATHG.objects.get(number=number)
            instance = ATHG.objects.get(number=number)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/TH/AThG.html', {'names': list})


def AThPS(request):
    list = ATHPS.objects.all()
    return render(request, 'firstyear/TH/AThPS.html', {'name': list})


def AThPAdd(request):
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            Cdate = ATHPS(ExNo=ExNo, semestery=semestery, publish=publish, lprice=lprice)
            Cdate.save()
            return redirect('AThPS')

    return render(request, 'firstyear/TH/AThPAdd.html')


def AThPM(request, ExNo, semestery):
    list = ATHPS.objects.get(ExNo=ExNo, semestery=semestery)
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            list.ExNo = ExNo
            list.semestery = semestery
            list.lprice = lprice
            list.publish = publish
            list.save()
        if 'delete' in request.POST:
            list.delete()
            return redirect('AThPS')

    return render(request, 'firstyear/TH/AThPM.html', {'name': list})


def AThP(request, ExNo, semestery):
    PreviosS = ATHPS.objects.get(ExNo=ExNo, semestery=semestery)
    list = ATHP.objects.filter(PreviosS=PreviosS)
    if request.method == "POST":
        if 'add' in request.POST:
            question = request.POST.get('question')
            ans1 = request.POST.get('ans1')
            ans2 = request.POST.get('ans2')
            ans3 = request.POST.get('ans3')
            ans4 = request.POST.get('ans4')
            why = request.POST.get('why')
            No_true = request.POST.get('No')
            number = request.POST.get('number')
            Cdate = ATHP(PreviosS=PreviosS, question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why,
                         No_true=No_true, number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = ATHP.objects.get(number=number, PreviosS=PreviosS)
            instance = ATHP.objects.filter(number=number, PreviosS=PreviosS)
            instance.delete()
            member.delete()
    return render(request, 'firstyear/TH/AThP.html', {'names': list})

def Statement(requrst):
    return render(requrst,'firstyear/Statement/Statement.html')
def WStatement(requrst):
    return render(requrst,'firstyear/Statement/WStatement.html')
def AStatement(requrst):
    return render(requrst,'firstyear/Statement/AStatement.html')

def WTStatementM(request):
    list = WTS.objects.all()
    return render(request, 'firstyear/Statement/WTStatementM.html', {'name': list})


def WTStatementE(request, number):
    list = WTS.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('WTStatementM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('WTStatementM')
    return render(request,'firstyear/Statement/WTStatementE.html', {'name': list})


def WTStatement(request):
    list = WTS.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = WTS.objects.create(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                                          publish=publish)
                Cdate.save()
                return redirect("WTStatementM")

    return render(request, 'firstyear/Statement/WTStatement.html', {'names': list, 'form': file})

def WPStatementM(request):
    list = WPS.objects.all()
    return render(request, 'firstyear/Statement/WPStatementM.html', {'name': list})


def WPStatementE(request, number):
    list = WPS.objects.get(number=number)
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('WPStatementM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('WPStatementM')
    return render(request,'firstyear/Statement/WPStatementE.html', {'name': list})


def WPStatement(request):
    list = WPS.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = WPS.objects.create(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                                          publish=publish)
                Cdate.save()
                return redirect("WPStatementM")

    return render(request, 'firstyear/Statement/WPStatement.html', {'names': list, 'form': file})


def WGStatementM(request):
    list = WGS.objects.first()
    return render(request,  'firstyear/Statement/WGStatementM.html', {'name': list})


def WGStatement(request):
    list = WGS.objects.first()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                publish = bool(request.POST.get('check'))
                Cdate = WGS(lname=name, lfile=request.FILES['file'], lprice=price, publish=publish)
                Cdate.save()
                return redirect('WGStatementM')
    return render(request, 'firstyear/Statement/WGStatement.html', {'names': list, 'form': file})


def WGStatementE(request):
    list = WGS.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('WGStatementM')

    if 'delete' in request.POST:
        member = WGS.objects.all()
        member.delete()
        return redirect('WGStatementM')

    return render(request, 'firstyear/Statement/WGStatementE.html', {'name': list})


def WPPStatementM(request):
    list = WPPS.objects.all()
    return render(request, 'firstyear/Statement/WPPStatementM.html', {'name': list})


def WPPStatementE(request, pyear, number):
    list = WPPS.objects.get(pyear=pyear, number=number)
    print(list)
    if 'add' in request.POST:
        pyear = request.POST.get('pyear')
        price = request.POST.get('price')
        number = request.POST.get('number')
        publish = bool(request.POST.get('check'))
        list.pyear = pyear
        list.publish = publish
        list.lprice = price
        list.namber = number
        list.save()
        return redirect('WPPStatementM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('WPPStatementM')
    return render(request, 'firstyear/Statement/WPPStatementE.html', {'name': list})


def WPPStatement(request):
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                pyear = request.POST.get('pyear')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = WPPS(pyear=pyear, lfile=request.FILES['file'], lprice=price, number=number, publish=publish)
                Cdate.save()
                return redirect('WPPStatementM')

    return render(request, 'firstyear/Statement/WPPStatement.html', {'form': file})

