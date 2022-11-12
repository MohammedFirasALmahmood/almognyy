from django.db import models
from manager.models import Student

# Create your models here.

class AGrammer31(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA3/AGrammer1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)

class AGrammer31Connent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(AGrammer31,on_delete=models.CASCADE)

class AGrammar34M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)

class AGrammar34MConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(AGrammar34M,on_delete=models.CASCADE)

class AGrammer34(models.Model):
    ExNo = models.ForeignKey(AGrammar34M, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']


class AMorphology31(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA3/AMorphology1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')

class AMorphology31Connent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(AMorphology31,on_delete=models.CASCADE)

class AMorphology34M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering = ['number']
class AMorphology34MConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(AMorphology34M,on_delete=models.CASCADE)



class AMorphology34(models.Model):
    ExNo = models.ForeignKey(AMorphology34M, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']


class AGMA3GoldenM(models.Model):
    name = models.TextField(max_length=100,null=False,default="0")
    publish = models.BooleanField()
    lprice = models.IntegerField(default=1)



class AGMA3Golden(models.Model):
    ExNo = models.ForeignKey(AGMA3GoldenM, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']


class AGMA3PriveosS(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    semestery = models.IntegerField(default=1, null=False, blank=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['ExNo', 'semestery']

class AGMA3PriveosSConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(AGMA3PriveosS,on_delete=models.CASCADE)


class AGMA3Priveos(models.Model):
    PreviosS = models.ForeignKey(AGMA3PriveosS, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']

class AQuranSciences(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='QuranSciences/AQuranSciences')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)

class AQuranSciencesConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(AQuranSciences,on_delete=models.CASCADE)


class HQuranSciences(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='QuranSciences/HQuranSciences')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)

class HQuranSciencesConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(HQuranSciences,on_delete=models.CASCADE)


class Maryam(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='QuranSciences/Maryam')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)

class MaryamConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(Maryam,on_delete=models.CASCADE)


class AMM(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='QuranSciences/AMM')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)

class AMMConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(AMM,on_delete=models.CASCADE)


class GQuranSciencesM(models.Model):
    name = models.TextField(max_length=100,null=False,default="0")
    publish = models.BooleanField()
    lprice = models.IntegerField(default=1)



class GQuranSciences(models.Model):
    ExNo = models.ForeignKey(GQuranSciencesM, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']


class PQuranSciencesS(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    semestery = models.IntegerField(default=1, null=False, blank=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['ExNo', 'semestery']

class PQuranSciencesSConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(PQuranSciencesS,on_delete=models.CASCADE)


class PQuranSciences(models.Model):
    PreviosS = models.ForeignKey(PQuranSciencesS, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']

class AIslamicLiterature(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='IslamicLiterature/AIslamicLiterature')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)

class AIslamicLiteratureConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(AIslamicLiterature,on_delete=models.CASCADE)


class HIslamicLiterature(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='IslamicLiterature/HIslamicLiterature')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)

class HIslamicLiteratureConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(HIslamicLiterature,on_delete=models.CASCADE)


class GIslamicLiterature(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='IslamicLiterature/GIslamicLiterature')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class PIslamicLiterature(models.Model):
    pyear = models.IntegerField(default=0, null=False)
    lfile = models.FileField(upload_to='IslamicLiterature/PIslamicLiterature')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['pyear', 'number']

class PIslamicLiteratureConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(PIslamicLiterature,on_delete=models.CASCADE)
# ------------------------------------Semantics-------------------------------------

class  WTSemantics(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Semantics/WTSemantics')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)

class WTSemanticsConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(WTSemantics,on_delete=models.CASCADE)



class WPSemantics(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Semantics/WPSemantics')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)

class WPSemanticsConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(WPSemantics,on_delete=models.CASCADE)


class WGSemantics(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Semantics/WGSemantics')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class WPPSemantics(models.Model):
    pyear = models.IntegerField(default=0, null=False)
    lfile = models.FileField(upload_to='Semantics/WPPSemantics')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['pyear', 'number']

class WPPSemanticsConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(WPPSemantics,on_delete=models.CASCADE)


class ATSemantics1(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Semantics/ATSemantics1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')

class ATSemantics1Connent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(ATSemantics1,on_delete=models.CASCADE)

class ATSemantics4M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering = ['number']


class ATSemantics4MConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(ATSemantics4M,on_delete=models.CASCADE)

class ATSemantics4(models.Model):
    ExNo = models.ForeignKey(ATSemantics4M, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']

class APSemantics1(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Semantics/APSemantics1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')

class APSemantics1Connent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(APSemantics1,on_delete=models.CASCADE)



class APSemantics4M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering = ['number']

class APSemantics4MConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(APSemantics4M,on_delete=models.CASCADE)


class APSemantics4(models.Model):
    ExNo = models.ForeignKey(APSemantics4M, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']

class AGSemanticsM(models.Model):
    name = models.TextField(max_length=100, null=False, default="0")
    publish = models.BooleanField()
    lprice = models.IntegerField(default=1)

class AGSemantics(models.Model):
    ExNo = models.ForeignKey(AGSemanticsM, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']


class APPSemanticsS(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    semestery = models.IntegerField(default=1, null=False, blank=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['ExNo', 'semestery']

class APPSemanticsSConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(APPSemanticsS,on_delete=models.CASCADE)


class APPSemantics(models.Model):
    PreviosS = models.ForeignKey(APPSemanticsS, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']

# -----------------------EN3-----------------------------------------------------
class AE31(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='AE3/AE31')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')

class AE31Connent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(AE31,on_delete=models.CASCADE)

class AE34M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering = ['number']


class AE34MConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(AE34M,on_delete=models.CASCADE)

class AE34(models.Model):
    ExNo = models.ForeignKey(AE34M, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']
class AE3PS(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    semestery = models.IntegerField(default=1, null=False, blank=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['ExNo', 'semestery']

class AE3PSConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(AE3PS,on_delete=models.CASCADE)

class AE3P(models.Model):
    PreviosS = models.ForeignKey(AE3PS, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']

# ---------------------------Persian--------------------------------------------

class Persian(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='AE3/AE31')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')

class PersianConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(Persian,on_delete=models.CASCADE)


#---------------History2--------------------------------------------------------
class History21(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Statement/APStatement1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')

class History21Connent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(History21,on_delete=models.CASCADE)



class History24M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering = ['number']

class History24MConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(History24M,on_delete=models.CASCADE)


class History24(models.Model):
    ExNo = models.ForeignKey(History24M, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']

class GHistory2M(models.Model):
    name = models.TextField(max_length=100, null=False, default="0")
    publish = models.BooleanField()
    lprice = models.IntegerField(default=1)

class GHistory2(models.Model):
    ExNo = models.ForeignKey(GHistory2M, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']


class PHistory2S(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    semestery = models.IntegerField(default=1, null=False, blank=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['ExNo', 'semestery']

class PHistory2SConnent(models.Model):
    user = models.ForeignKey(Student,on_delete=models.CASCADE)
    lecture = models.ForeignKey(PHistory2S,on_delete=models.CASCADE)


class PHistory2(models.Model):
    PreviosS = models.ForeignKey(PHistory2S, on_delete=models.CASCADE, default=1)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)

    class Meta:
        ordering = ['number']

