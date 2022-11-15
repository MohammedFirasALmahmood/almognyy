from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import AGrammer31 as AG31
from .models import AGrammer34 as AG34
from .models import AGrammar34M as AG34M
from .models import AMorphology34 as AM34
from .models import AMorphology34M as AM34M
from .models import AMorphology31 as AM31
from .models import AGMA3GoldenM as AGMAG3M
from .models import AGMA3Golden as AGMAG3
from .models import AGMA3Priveos as AGMA3P
from .models import AGMA3PriveosS as AGMA3PS
from .models import AQuranSciences as AQ
from .models import HQuranSciences as HQ
from .models import Maryam as Ma
from .models import AMM as Am
from .models import QuranSciencesG as QG
from .models import QuranSciencesP as QP
from .models import AIslamicLiterature as AI
from .models import HIslamicLiterature as HI
from .models import GIslamicLiterature as GI
from .models import PIslamicLiterature as PI
from .models import PIslamicLiterature as PI
from .models import WTSemantics as WTS
from .models import WPSemantics as WPS
from .models import WGSemantics as WGS
from .models import WPPSemantics as WPPS
from .models import APSemantics1 as APS1
from .models import APSemantics4 as APS4
from .models import APSemantics4M as APS4M
from .models import ATSemantics1 as ATS1
from .models import ATSemantics4 as ATS4
from .models import ATSemantics4M as ATS4M
from .models import AGSemantics as AGS
from .models import AGSemanticsM as AGSM
from .models import APPSemantics as APPS
from .models import APPSemanticsS as APPSS
from .models import AE31
from .models import AE34
from .models import AE34M
from .models import AE3P
from .models import AE3PS
from .models import Persian as Per
from .models import History21 as H1
from .models import History24 as H4
from .models import History24M as H4M
from .models import GHistory2 as GH
from .models import GHistory2M as GHM
from .models import PHistory2 as PH
from .models import PHistory2S as PHS

class Form1(forms.Form):
    file = forms.FileField()

# Create your views here.
def firstsemester(request):
    return render(request, 'secoundyear/firstsemester.html')


def AGMA3(request):
    return render(request, 'secoundyear/AGMA3/AGMA3.html')


def AGrammer3(request):
    return render(request, 'secoundyear/AGMA3/AGrammar3.html', )


def AGrammar31M(request):
    list = AG31.objects.all()

    return render(request, 'secoundyear/AGMA3/AGrammar31M.html', {'name': list})


def AGrammer31(request):
    list = AG31.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AG31(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AGrammar31M')

    return render(request, 'secoundyear/AGMA3/AGrammar31.html', {'names': list, 'form': file})


def AGrammar31E(request, number):
    list = AG31.objects.get(number=number)
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
        return redirect('AGrammar31M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AGrammar31M')

    return render(request, 'secoundyear/AGMA3/AGrammar31E.html', {'name': list})


def AGrammar34M(request):
    list = AG34M.objects.all()

    return render(request, 'secoundyear/AGMA3/AGrammar34M.html', {'names': list})


def AGrammar34E(request, number):
    list = AG34M.objects.get(number=number)
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
        return redirect('AGrammar34M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AGrammar34M')

    return render(request, 'secoundyear/AGMA3/AGrammar34E.html', {'name': list})


def AGrammar34Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AG34M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AGrammar34M')
    return render(request, 'secoundyear/AGMA3/AGrammar34Add.html')


def AGrammar34(request, number):
    db = AG34M.objects.get(number=number)
    list = AG34.objects.filter(ExNo=db)
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
            Cdate = AG34(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AG34.objects.get(number=number, ExNo=db)
            instance = AG34.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'secoundyear/AGMA3/AGrammar34.html', {'names': list})



def AMorphology3(request):
    return render(request, 'secoundyear/AGMA3/AMorphology3.html')


def AMorphology31M(request):
    list = AM31.objects.all()

    return render(request, 'secoundyear/AGMA3/AMorphology31M.html', {'name': list})


def AMorphology31(request):
    list = AM31.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AM31(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AMorphology31M')

    return render(request, 'secoundyear/AGMA3/AMorphology31.html', {'names': list, 'form': file})


def AMorphology31E(request, number):
    list = AM31.objects.get(number=number)
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
        return redirect('AMorphology31M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AMorphology31M')

    return render(request, 'secoundyear/AGMA3/AMorphology31E.html', {'name': list})


def AMorphology34M(request):
    list = AM34M.objects.all()

    return render(request, 'secoundyear/AGMA3/AMorphology34M.html', {'names': list})


def AMorphology34E(request, number):
    list = AM34M.objects.get(number=number)
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
        return redirect('AMorphology34M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AMorphology34M')

    return render(request, 'secoundyear/AGMA3/AMorphology34E.html', {'name': list})


def AMorphology34Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AM34M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AMorphology34M')
    return render(request, 'secoundyear/AGMA3/AMorphology34Add.html')


def AMorphology34(request, number):
    db = AM34M.objects.get(number=number)
    list = AM34.objects.filter(ExNo=db)
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
            Cdate = AM34(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AM34.objects.get(number=number, ExNo=db)
            instance = AM34.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'secoundyear/AGMA3/AMorphology34.html', {'names': list})


def AGMA3GoldenM(request):
    list = AGMAG3M.objects.first()

    return render(request, 'secoundyear/AGMA3/AGMA3GoldenM.html', {'names': list})


def AGMA3GoldenE(request):
    list = AGMAG3M.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.lprice = price
        list.publish = publish
        list.save()
        return redirect('AGMA3GoldenM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AGMA3GoldenM')

    return render(request, 'secoundyear/AGMA3/AGMA3GoldenE.html', {'name': list})


def AGMA3GoldenAdd(request):
    if request.method == "POST":
        name = request.POST.get("name")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AGMAG3M(name=name, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AGMA3GoldenM')
    return render(request, 'secoundyear/AGMA3/AGMA3GoldenAdd.html')


def AGMA3Golden(request):
    db = AGMAG3M.objects.first()
    list = AGMAG3.objects.all()
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

            Cdate = AGMAG3(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                          number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AGMAG3.objects.get(number=number)
            instance = AGMAG3.objects.get(number=number)
            instance.delete()
            member.delete()
    return render(request, 'secoundyear/AGMA3/AGMA3Golden.html', {'names': list})


def AGMA3PriveosS(request):
    list = AGMA3PS.objects.all()
    return render(request, 'secoundyear/AGMA3/AGMA3PriveosS.html', {'name': list})


def AGMA3PriveosAdd(request):
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            Cdate = AGMA3PS(ExNo=ExNo, semestery=semestery, publish=publish, lprice=lprice)
            Cdate.save()
            return redirect('AGMA3PriveosS')

    return render(request, 'secoundyear/AGMA3/AGMA3PriveosAdd.html')


def AGMA3PriveosM(request, ExNo, semestery):
    list = AGMA3PS.objects.get(ExNo=ExNo, semestery=semestery)
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
            return redirect('AGMA3PriveosS')

    return render(request, 'secoundyear/AGMA3/AGMA3PriveosM.html', {'name': list})


def AGMA3Priveos(request, ExNo, semestery):
    PreviosS = AGMA3PS.objects.get(ExNo=ExNo, semestery=semestery)
    list = AGMA3P.objects.filter(PreviosS=PreviosS)
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
            Cdate = AGMA3P(PreviosS=PreviosS, question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why,
                          No_true=No_true, number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AGMA3P.objects.get(number=number, PreviosS=PreviosS)
            instance = AGMA3P.objects.filter(number=number, PreviosS=PreviosS)
            instance.delete()
            member.delete()

    return render(request, 'secoundyear/AGMA3/AGMA3Priveos.html', {'names': list})



def QuranSciences(request):
    return render(request, 'secoundyear/QuranSciences/QuranSciences.html')


def AQuranSciencesM(request):
    list = AQ.objects.all()

    return render(request, 'secoundyear/QuranSciences/AQuranSciencesM.html', {'name': list})


def AQuranSciences(request):
    list = AQ.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AQ(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AQuranSciencesM')

    return render(request, 'secoundyear/QuranSciences/AQuranSciences.html', {'names': list, 'form': file})


def AQuranSciencesE(request, number):
    list = AQ.objects.get(number=number)
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
        return redirect('AQuranSciencesM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AQuranSciencesM')

    return render(request, 'secoundyear/QuranSciences/AQuranSciencesE.html', {'name': list})


def HQuranSciencesM(request):
    list = HQ.objects.all()

    return render(request, 'secoundyear/QuranSciences/HQuranSciencesM.html', {'name': list})


def HQuranSciences(request):
    list = HQ.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = HQ(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('HQuranSciencesM')

    return render(request, 'secoundyear/QuranSciences/HQuranSciences.html', {'names': list, 'form': file})


def HQuranSciencesE(request, number):
    list = HQ.objects.get(number=number)
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
        return redirect('HQuranSciencesM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('HQuranSciencesM')

    return render(request, 'secoundyear/QuranSciences/HQuranSciencesE.html', {'name': list})


def MaryamM(request):
    list = Ma.objects.all()

    return render(request, 'secoundyear/QuranSciences/MaryamM.html', {'name': list})


def Maryam(request):
    list = Ma.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = Ma(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('MaryamM')

    return render(request, 'secoundyear/QuranSciences/Maryam.html', {'names': list, 'form': file})


def MaryamE(request, number):
    list = Ma.objects.get(number=number)
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
        return redirect('MaryamM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('MaryamM')

    return render(request, 'secoundyear/QuranSciences/MaryamE.html', {'name': list})


def AMMM(request):
    list = Am.objects.all()

    return render(request, 'secoundyear/QuranSciences/AMMM.html', {'name': list})


def AMM(request):
    list = Am.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = Am(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AMMM')

    return render(request, 'secoundyear/QuranSciences/AMM.html', {'names': list, 'form': file})


def AMME(request, number):
    list = Am.objects.get(number=number)
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
        return redirect('AMMM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AMMM')

    return render(request, 'secoundyear/QuranSciences/AMME.html', {'name': list})


def QuranSciencesGM(request):
    list = QG.objects.first()
    return render(request, 'secoundyear/QuranSciences/QuranSciencesGM.html', {'name': list})


def QuranSciencesG(request):
    list = QG.objects.first()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                publish = bool(request.POST.get('check'))
                Cdate = QG(lname=name, lfile=request.FILES['file'], lprice=price, publish=publish)
                Cdate.save()
                return redirect('QuranSciencesGM')
    return render(request, 'secoundyear/QuranSciences/QuranSciencesG.html', {'names': list, 'form': file})


def QuranSciencesGE(request):
    list = QG.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('QuranSciencesGM')

    if 'delete' in request.POST:
        member = QG.objects.all()
        member.delete()
        return redirect('QuranSciencesGM')

    return render(request, 'secoundyear/QuranSciences/QuranSciencesGE.html', {'name': list})


def QuranSciencesPM(request):
    list = QP.objects.all()
    return render(request, 'secoundyear/QuranSciences/QuranSciencesPM.html', {'name': list})


def QuranSciencesPE(request, pyear, number):
    list = QP.objects.get(pyear=pyear, number=number)
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
        return redirect('QuranSciencesPM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('QuranSciencesPM')
    return render(request, 'secoundyear/QuranSciences/QuranSciencesPE.html', {'name': list})


def QuranSciencesP(request):
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                pyear = request.POST.get('pyear')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = QP(pyear=pyear, lfile=request.FILES['file'], lprice=price, number=number, publish=publish)
                Cdate.save()
                return redirect('QuranSciencesPM')

    return render(request, 'secoundyear/QuranSciences/QuranSciencesP.html', {'form': file})


#----------------------------IslamicLiterature----------------------------------------

def IslamicLiterature(request):

    return render(request, 'secoundyear/IslamicLiterature/IslamicLiterature.html')


def AIslamicLiteratureM(request):
    list = AI.objects.all()

    return render(request, 'secoundyear/IslamicLiterature/AIslamicLiteratureM.html', {'name': list})


def AIslamicLiterature(request):
    list = AI.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AI(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AIslamicLiteratureM')

    return render(request, 'secoundyear/IslamicLiterature/AIslamicLiterature.html', {'names': list, 'form': file})


def AIslamicLiteratureE(request, number):
    list = AI.objects.get(number=number)
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
        return redirect('AIslamicLiteratureM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AIslamicLiteratureM')

    return render(request, 'secoundyear/IslamicLiterature/AIslamicLiteratureE.html', {'name': list})


def HIslamicLiteratureM(request):
    list = HI.objects.all()

    return render(request, 'secoundyear/IslamicLiterature/HIslamicLiteratureM.html', {'name': list})


def HIslamicLiterature(request):
    list = HI.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = HI(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('HIslamicLiteratureM')

    return render(request, 'secoundyear/IslamicLiterature/HIslamicLiterature.html', {'names': list, 'form': file})


def HIslamicLiteratureE(request, number):
    list = HI.objects.get(number=number)
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
        return redirect('HIslamicLiteratureM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('HIslamicLiteratureM')

    return render(request, 'secoundyear/IslamicLiterature/HIslamicLiteratureE.html', {'name': list})


def IslamicLiteratureGM(request):
    list = GI.objects.first()
    return render(request, 'secoundyear/IslamicLiterature/IslamicLiteratureGM.html', {'name': list})


def IslamicLiteratureG(request):
    list = GI.objects.first()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                publish = bool(request.POST.get('check'))
                Cdate = GI(lname=name, lfile=request.FILES['file'], lprice=price, publish=publish)
                Cdate.save()
                return redirect('IslamicLiteratureGM')
    return render(request, 'secoundyear/IslamicLiterature/IslamicLiteratureG.html', {'names': list, 'form': file})


def IslamicLiteratureGE(request):
    list = GI.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('IslamicLiteratureGM')

    if 'delete' in request.POST:
        member = GI.objects.all()
        member.delete()
        return redirect('IslamicLiteratureGM')

    return render(request, 'secoundyear/IslamicLiterature/IslamicLiteratureGE.html', {'name': list})


def IslamicLiteraturePM(request):
    list = PI.objects.all()
    return render(request, 'secoundyear/IslamicLiterature/IslamicLiteraturePM.html', {'name': list})


def IslamicLiteraturePE(request, pyear, number):
    list = PI.objects.get(pyear=pyear, number=number)
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
        return redirect('IslamicLiteraturePM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('IslamicLiteraturePM')
    return render(request, 'secoundyear/IslamicLiterature/IslamicLiteraturePE.html', {'name': list})


def IslamicLiteratureP(request):
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                pyear = request.POST.get('pyear')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = PI(pyear=pyear, lfile=request.FILES['file'], lprice=price, number=number, publish=publish)
                Cdate.save()
                return redirect('IslamicLiteraturePM')

    return render(request, 'secoundyear/IslamicLiterature/IslamicLiteratureP.html', {'form': file})

#--------------------------------------------------------------------------------------------------------------

def Semantics(requrst):
    return render(requrst,'secoundyear/Semantics/Semantics.html')
def WSemantics(requrst):
    return render(requrst,'secoundyear/Semantics/WSemantics.html')

def WTSemanticsM(request):
    list = WTS.objects.all()
    return render(request, 'secoundyear/Semantics/WTSemanticsM.html', {'name': list})


def WTSemanticsE(request, number):
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
        return redirect('WTSemanticsM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('WTSemanticsM')
    return render(request,'secoundyear/Semantics/WTSemanticsE.html', {'name': list})


def WTSemantics(request):
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
                return redirect("WTSemanticsM")

    return render(request, 'secoundyear/Semantics/WTSemantics.html', {'names': list, 'form': file})

def WPSemanticsM(request):
    list = WPS.objects.all()
    return render(request, 'secoundyear/Semantics/WPSemanticsM.html', {'name': list})


def WPSemanticsE(request, number):
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
        return redirect('WPSemanticsM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('WPSemanticsM')
    return render(request,'secoundyear/Semantics/WPSemanticsE.html', {'name': list})


def WPSemantics(request):
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
                return redirect("WPSemanticsM")

    return render(request, 'secoundyear/Semantics/WPSemantics.html', {'names': list, 'form': file})


def WGSemanticsM(request):
    list = WGS.objects.first()
    return render(request,  'secoundyear/Semantics/WGSemanticsM.html', {'name': list})


def WGSemantics(request):
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
                return redirect('WGSemanticsM')
    return render(request, 'secoundyear/Semantics/WGSemantics.html', {'names': list, 'form': file})


def WGSemanticsE(request):
    list = WGS.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.lname = name
        list.publish = publish
        list.lprice = price
        list.save()
        return redirect('WGSemanticsM')

    if 'delete' in request.POST:
        member = WGS.objects.all()
        member.delete()
        return redirect('WGSemanticsM')

    return render(request, 'secoundyear/Semantics/WGSemanticsE.html', {'name': list})


def WPPSemanticsM(request):
    list = WPPS.objects.all()
    return render(request, 'secoundyear/Semantics/WPPSemanticsM.html', {'name': list})


def WPPSemanticsE(request, pyear, number):
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
        return redirect('WPPSemanticsM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('WPPSemanticsM')
    return render(request, 'secoundyear/Semantics/WPPSemanticsE.html', {'name': list})


def WPPSemantics(request):
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
                return redirect('WPPSemanticsM')

    return render(request, 'secoundyear/Semantics/WPPSemantics.html', {'form': file})


def ASemantics(requrst):
    return render(requrst,'secoundyear/Semantics/ASemantics.html')


def ATSemantics(requrst):
    return render(requrst,'secoundyear/Semantics/ATSemantics.html')

def APSemantics(requrst):
    return render(requrst,'secoundyear/Semantics/APSemantics.html')


def ATSemantics1M(request):
    list = ATS1.objects.all()

    return render(request, 'secoundyear/Semantics/ATSemantics1M.html', {'name': list})


def ATSemantics1(request):
    list = ATS1.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = ATS1(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('ATSemantics1M')

    return render(request, 'secoundyear/Semantics/ATSemantics1.html', {'names': list, 'form': file})


def ATSemantics1E(request, number):
    list = ATS1.objects.get(number=number)
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
        return redirect('ATSemantics1M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('ATSemantics1M')

    return render(request, 'secoundyear/Semantics/ATSemantics1E.html', {'name': list})


def ATSemantics4M(request):
    list = ATS4M.objects.all()

    return render(request, 'secoundyear/Semantics/ATSemantics4M.html', {'names': list})


def ATSemantics4E(request, number):
    list = ATS4M.objects.get(number=number)
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
        return redirect('ATSemantics4M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('ATSemantics4M')

    return render(request, 'secoundyear/Semantics/ATSemantics4E.html', {'name': list})


def ATSemantics4Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = ATS4M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('ATSemantics4M')
    return render(request, 'secoundyear/Semantics/ATSemantics4Add.html')


def ATSemantics4(request, number):
    db = ATS4M.objects.get(number=number)
    list = ATS4.objects.filter(ExNo=db)
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
            Cdate = ATS4(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = ATS4.objects.get(number=number, ExNo=db)
            instance = ATS4.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'secoundyear/Semantics/ATSemantics4.html', {'names': list})




def APSemantics1M(request):
    list = APS1.objects.all()

    return render(request, 'secoundyear/Semantics/APSemantics1M.html', {'name': list})


def APSemantics1(request):
    list = APS1.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = APS1(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('APSemantics1M')

    return render(request, 'secoundyear/Semantics/APSemantics1.html', {'names': list, 'form': file})


def APSemantics1E(request, number):
    list = APS1.objects.get(number=number)
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
        return redirect('APSemantics1M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('APSemantics1M')

    return render(request, 'secoundyear/Semantics/APSemantics1E.html', {'name': list})


def APSemantics4M(request):
    list = APS4M.objects.all()

    return render(request, 'secoundyear/Semantics/APSemantics4M.html', {'names': list})


def APSemantics4E(request, number):
    list = APS4M.objects.get(number=number)
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
        return redirect('APSemantics4M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('APSemantics4M')

    return render(request, 'secoundyear/Semantics/APSemantics4E.html', {'name': list})


def APSemantics4Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = APS4M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('APSemantics4M')
    return render(request, 'secoundyear/Semantics/APSemantics4Add.html')


def APSemantics4(request, number):
    db = APS4M.objects.get(number=number)
    list = APS4.objects.filter(ExNo=db)
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
            Cdate = APS4(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = APS4.objects.get(number=number, ExNo=db)
            instance = APS4.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'secoundyear/Semantics/APSemantics4.html', {'names': list})


def AGSemanticsM(request):
    list = AGSM.objects.first()

    return render(request, 'secoundyear/Semantics/AGSemanticsM.html', {'names': list})


def AGSemanticsE(request):
    list = AGSM.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.lprice = price
        list.publish = publish
        list.save()
        return redirect('AGSemanticsM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AGSemanticsM')

    return render(request, 'secoundyear/Semantics/AGSemanticsE.html', {'names': list})


def AGSemanticsAdd(request):
    if request.method == "POST":
        name = request.POST.get("name")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AGSM(name=name, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AGSemanticsM')
    return render(request, 'secoundyear/Semantics/AGSemanticsAdd.html', {'names': list})


def AGSemantics(request):
    db = AGSM.objects.first()
    list = AGS.objects.all()
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

            Cdate = AGS(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                          number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AGS.objects.get(number=number)
            instance = AGS.objects.get(number=number)
            instance.delete()
            member.delete()
    return render(request, 'secoundyear/Semantics/AGSemantics.html', {'names': list})


def APPSemanticsS(request):
    list = APPSS.objects.all()
    return render(request, 'secoundyear/Semantics/APPSemanticsS.html', {'names': list})


def APPSemanticsAdd(request):
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            Cdate = APPSS(ExNo=ExNo, semestery=semestery, publish=publish, lprice=lprice)
            Cdate.save()
            return redirect('AGMAPriveosS')

    return render(request, 'secoundyear/Semantics/APPSemanticsAdd.html', {'names': list})


def APPSemanticsM(request, ExNo, semestery):
    list = APPSS.objects.get(ExNo=ExNo, semestery=semestery)
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
            return redirect('APPSemanticsS')

    return render(request, 'secoundyear/Semantics/APPSemanticsM.html', {'names': list})


def APPSemantics(request, ExNo, semestery):
    PreviosS = APPSS.objects.get(ExNo=ExNo, semestery=semestery)
    list = APPS.objects.filter(PreviosS=PreviosS)
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
            Cdate = APPS(PreviosS=PreviosS, question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why,
                          No_true=No_true, number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = APPS.objects.get(number=number, PreviosS=PreviosS)
            instance = APPS.objects.filter(number=number, PreviosS=PreviosS)
            instance.delete()
            member.delete()

    return render(request, 'secoundyear/Semantics/APPSemantics.html', {'names': list})
#---------------------------------------------------------------------------------------


def AEn3(request):
    return render(request, 'secoundyear/E3/AEn3.html')


def AEn31M(request):
    list = AE31.objects.all()

    return render(request, 'secoundyear/E3/AEn31M.html', {'name': list})


def AEn31(request):
    list = AE31.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = AE31(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AEn31M')

    return render(request, 'secoundyear/E3/AEn31.html', {'names': list, 'form': file})


def AEn31E(request, number):
    list = AE31.objects.get(number=number)
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
        return redirect('AEn31M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AEn31M')

    return render(request, 'secoundyear/E3/AEn31E.html', {'name': list})


def AEn34M(request):
    list = AE34M.objects.all()

    return render(request, 'secoundyear/E3/AEn34M.html', {'names': list})


def AEn34E(request, number):
    list = AE34M.objects.get(number=number)
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
        return redirect('AEn34M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AEn34M')

    return render(request, 'secoundyear/E3/AEn34E.html', {'name': list})


def AEn34Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = AE34M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AEn34M')
    return render(request, 'secoundyear/E3/AEn34Add.html')


def AEn34(request, number):
    db = AE34M.objects.get(number=number)
    list = AE34.objects.filter(ExNo=db)
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
            Cdate = AE34(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AE34.objects.get(number=number, ExNo=db)
            instance = AE34.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'secoundyear/E3/AEn34.html', {'names': list})


def AEn3PS(request):
    list = AE3PS.objects.all()
    return render(request, 'secoundyear/E3/AEn3PS.html', {'name': list})


def AEn3PAdd(request):
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            Cdate = AE3PS(ExNo=ExNo, semestery=semestery, publish=publish, lprice=lprice)
            Cdate.save()
            return redirect('AEn3PS')

    return render(request, 'secoundyear/E3/AEn3PAdd.html')


def AEn3PM(request, ExNo, semestery):
    list = AE3PS.objects.get(ExNo=ExNo, semestery=semestery)
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
            return redirect('AEn3PS')

    return render(request, 'secoundyear/E3/AEn3PM.html', {'name': list})


def AEn3P(request, ExNo, semestery):
    PreviosS = AE3PS.objects.get(ExNo=ExNo, semestery=semestery)
    list = AE3P.objects.filter(PreviosS=PreviosS)
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
            Cdate = AE3P(PreviosS=PreviosS, question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why,
                        No_true=No_true, number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AE3P.objects.get(number=number, PreviosS=PreviosS)
            instance = AE3P.objects.filter(number=number, PreviosS=PreviosS)
            instance.delete()
            member.delete()
    return render(request, 'secoundyear/E3/AEn3P.html', {'names': list})

#-------------------------------------------------Persian---------------------------------------------------------------


def PersianM(request):
    list = Per.objects.all()

    return render(request, 'secoundyear/Persian/PersianM.html', {'name': list})


def Persian(request):
    list = Per.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = Per(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('PersianM')

    return render(request, 'secoundyear/Persian/Persian.html', {'names': list, 'form': file})


def PersianE(request, number):
    list = Per.objects.get(number=number)
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
        return redirect('PersianM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('PersianM')

    return render(request, 'secoundyear/Persian/PersianE.html', {'name': list})



#----------------------------political history2-------------------------------------------------------------------------


def AHistory2(request):
    return render(request, 'secoundyear/History2/AHistory2.html')


def AHistory21M(request):
    list = H1.objects.all()

    return render(request, 'secoundyear/History2/AHistory21M.html', {'name': list})


def AHistory21(request):
    list = H1.objects.all()
    file = Form1(request.POST, request.FILES)
    if request.method == "POST":
        if 'add' in request.POST:
            if file.is_valid():
                name = request.POST.get('name')
                price = request.POST.get('price')
                number = request.POST.get('number')
                publish = bool(request.POST.get('check'))
                Cdate = H1(lname=name, lfile=request.FILES['file'], lprice=price, number=number,
                            publish=publish)
                Cdate.save()
                return redirect('AHistory21M')

    return render(request, 'secoundyear/History2/AHistory21.html', {'names': list, 'form': file})


def AHistory21E(request, number):
    list = H1.objects.get(number=number)
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
        return redirect('AHistory21M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AHistory21M')

    return render(request, 'secoundyear/History2/AHistory21E.html', {'name': list})


def AHistory24M(request):
    list = H4M.objects.all()

    return render(request, 'secoundyear/History2/AHistory24M.html', {'names': list})


def AHistory24E(request, number):
    list = H4M.objects.get(number=number)
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
        return redirect('AHistory24M')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AHistory24M')

    return render(request, 'secoundyear/History2/AHistory24E.html', {'name': list})


def AHistory24Add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        number = request.POST.get("number")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = H4M(name=name, number=number, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AHistory24M')
    return render(request, 'secoundyear/History2/AHistory24Add.html')


def AHistory24(request, number):
    db = H4M.objects.get(number=number)
    list = H4.objects.filter(ExNo=db)
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
            Cdate = H4(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        ExNo=db,
                        number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = H4.objects.get(number=number, ExNo=db)
            instance = H4.objects.filter(number=number, ExNo=db)
            instance.delete()
            member.delete()

    return render(request, 'secoundyear/History2/AHistory24.html', {'names': list})


def AHistory2GM(request):
    list = GHM.objects.first()

    return render(request, 'secoundyear/History2/AHistory2GM.html', {'names': list})


def AHistory2GE(request):
    list = GHM.objects.first()
    if 'add' in request.POST:
        name = request.POST.get('name')
        price = request.POST.get('price')
        publish = bool(request.POST.get('check'))
        list.name = name
        list.lprice = price
        list.publish = publish
        list.save()
        return redirect('AHistory2GM')

    if 'delete' in request.POST:
        list.delete()
        return redirect('AHistory2GM')

    return render(request, 'secoundyear/History2/AHistory2GE.html', {'name': list})


def AHistory2GAdd(request):
    if request.method == "POST":
        name = request.POST.get("name")
        publish = bool(request.POST.get('check'))
        lprice = request.POST.get("price")
        Cdata = GHM(name=name, publish=publish, lprice=lprice)
        Cdata.save()
        return redirect('AHistory2GM')
    return render(request, 'secoundyear/History2/AHistory2GAdd.html')


def AHistory2G(request):
    db = GHM.objects.first()
    list = GH.objects.all()
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

            Cdate = GH(question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why, No_true=No_true,
                        number=number, ExNo=db)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = GH.objects.get(number=number)
            instance = GH.objects.get(number=number)
            instance.delete()
            member.delete()
    return render(request, 'secoundyear/History2/AHistory2G.html', {'names': list})


def AHistory2PS(request):
    list = PHS.objects.all()
    return render(request, 'secoundyear/History2/AHistory2PS.html', {'name': list})


def AHistory2PAdd(request):
    if request.method == "POST":
        if 'add' in request.POST:
            ExNo = request.POST.get('ExNo')
            semestery = request.POST.get('semestery')
            lprice = request.POST.get('price')
            publish = bool(request.POST.get('check'))
            Cdate = PHS(ExNo=ExNo, semestery=semestery, publish=publish, lprice=lprice)
            Cdate.save()
            return redirect('AHistory2PS')

    return render(request, 'secoundyear/History2/AHistory2PAdd.html')


def AHistory2PM(request, ExNo, semestery):
    list = PHS.objects.get(ExNo=ExNo, semestery=semestery)
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
            return redirect('AHistory2PS')

    return render(request, 'secoundyear/History2/AHistory2PM.html', {'name': list})


def AHistory2P(request, ExNo, semestery):
    PreviosS = AEPS.objects.get(ExNo=ExNo, semestery=semestery)
    list = PH.objects.filter(PreviosS=PreviosS)
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
            Cdate = PH(PreviosS=PreviosS, question=question, ans1=ans1, ans2=ans2, ans3=ans3, ans4=ans4, why=why,
                        No_true=No_true, number=number)
            Cdate.save()

        elif 'delete' in request.POST:
            number = request.POST.get("number")
            member = AEP.objects.get(number=number, PreviosS=PreviosS)
            instance = PH.objects.filter(number=number, PreviosS=PreviosS)
            instance.delete()
            member.delete()
    return render(request, 'secoundyear/History2/AHistory2P.html', {'names': list})

