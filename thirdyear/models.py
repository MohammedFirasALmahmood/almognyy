from django.db import models

from manager.models import Student
# Create your models here.

class AGrammer51(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA5/AGrammer1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class AGrammer51Connent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(AGrammer51, on_delete=models.CASCADE)


class AGrammar54M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)


class AGrammar54MConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(AGrammar54M, on_delete=models.CASCADE)


class AGrammer54(models.Model):
    ExNo = models.ForeignKey(AGrammar54M, on_delete=models.CASCADE, default=1)
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


class AMorphology51(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA5/AMorphology1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')


class AMorphology51Connent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(AMorphology51, on_delete=models.CASCADE)


class AMorphology54M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering = ['number']


class AMorphology54MConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(AMorphology54M, on_delete=models.CASCADE)


class AMorphology54(models.Model):
    ExNo = models.ForeignKey(AMorphology54M, on_delete=models.CASCADE, default=1)
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


class AGMA5GoldenM(models.Model):
    name = models.TextField(max_length=100, null=False, default="0")
    publish = models.BooleanField()
    lprice = models.IntegerField(default=1)


class AGMA5Golden(models.Model):
    ExNo = models.ForeignKey(AGMA5GoldenM, on_delete=models.CASCADE, default=1)
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


class AGMA5PriveosS(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    semestery = models.IntegerField(default=1, null=False, blank=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['ExNo', 'semestery']


class AGMA5PriveosSConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(AGMA5PriveosS, on_delete=models.CASCADE)


class AGMA5Priveos(models.Model):
    PreviosS = models.ForeignKey(AGMA5PriveosS, on_delete=models.CASCADE, default=1)
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


#--------------------------Philology----------------------------------------------------

class APhilology(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Philology/APhilology')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class APhilologyConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(APhilology, on_delete=models.CASCADE)


class HPhilology(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Philology/HPhilology')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class HPhilologyConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(HPhilology, on_delete=models.CASCADE)


class GPhilology(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Philology/GPhilology')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class PPhilology(models.Model):
    pyear = models.IntegerField(default=0, null=False)
    lfile = models.FileField(upload_to='Philology/PPhilology')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['pyear', 'number']


class PPhilologyConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(PPhilology, on_delete=models.CASCADE)

#--------------------------------------------AbbasiPoetry-------------------------------------------------------------


class AAbbasiPoetry(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='AbbasiPoetry/AAbbasiPoetry')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class AAbbasiPoetryConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(AAbbasiPoetry, on_delete=models.CASCADE)


class HAbbasiPoetry(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='AbbasiPoetry/HAbbasiPoetry')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class HAbbasiPoetryConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(HAbbasiPoetry, on_delete=models.CASCADE)


class GAbbasiPoetry(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='AbbasiPoetry/GAbbasiPoetry')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class PAbbasiPoetry(models.Model):
    pyear = models.IntegerField(default=0, null=False)
    lfile = models.FileField(upload_to='AbbasiPoetry/PAbbasiPoetry')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['pyear', 'number']


class PAbbasiPoetryConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(PAbbasiPoetry, on_delete=models.CASCADE)

#--------------------------------------------AndalusianPoetry-------------------------------------------------------------


class AAndalusianPoetry(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='AndalusianPoetry/AAndalusianPoetry')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class AAndalusianPoetryConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(AAndalusianPoetry, on_delete=models.CASCADE)


class HAndalusianPoetry(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='AndalusianPoetry/HAndalusianPoetry')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class HAndalusianPoetryConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(HAndalusianPoetry, on_delete=models.CASCADE)


class GAndalusianPoetry(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='AndalusianPoetry/GAndalusianPoetry')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class PAndalusianPoetry(models.Model):
    pyear = models.IntegerField(default=0, null=False)
    lfile = models.FileField(upload_to='AndalusianPoetry/PAndalusianPoetry')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['pyear', 'number']


class PAndalusianPoetryConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(PAndalusianPoetry, on_delete=models.CASCADE)
#------------------------------------------Critique----------------------------------------------------------

class ADohman1(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Critique/ADohman1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class ADohmanConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(ADohman1, on_delete=models.CASCADE)


class ADohman4M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)


class ADohman4MConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(ADohman4M, on_delete=models.CASCADE)


class ADohman4(models.Model):
    ExNo = models.ForeignKey(ADohman4M, on_delete=models.CASCADE, default=1)
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


class ANawal1(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Critique/ANawal1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')


class ANawal1Connent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(ANawal1, on_delete=models.CASCADE)


class ANawal4M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering = ['number']


class ANawal4MConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(ANawal4M, on_delete=models.CASCADE)


class ANawal4(models.Model):
    ExNo = models.ForeignKey(ANawal4M, on_delete=models.CASCADE, default=1)
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


class GCritiqueM(models.Model):
    name = models.TextField(max_length=100, null=False, default="0")
    publish = models.BooleanField()
    lprice = models.IntegerField(default=1)


class GCritique(models.Model):
    ExNo = models.ForeignKey(GCritiqueM, on_delete=models.CASCADE, default=1)
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


class PCritiqueS(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    semestery = models.IntegerField(default=1, null=False, blank=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['ExNo', 'semestery']


class PCritiqueSConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(PCritiqueS, on_delete=models.CASCADE)


class PCritique(models.Model):
    PreviosS = models.ForeignKey(PCritiqueS, on_delete=models.CASCADE, default=1)
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

# ---------------History3--------------------------------------------------------
class History31(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='History3/History31')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')


class History31Connent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(History31, on_delete=models.CASCADE)


class History34M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering = ['number']


class History34MConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(History34M, on_delete=models.CASCADE)


class History34(models.Model):
    ExNo = models.ForeignKey(History34M, on_delete=models.CASCADE, default=1)
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


class GHistory3M(models.Model):
    name = models.TextField(max_length=100, null=False, default="0")
    publish = models.BooleanField()
    lprice = models.IntegerField(default=1)


class GHistory3(models.Model):
    ExNo = models.ForeignKey(GHistory3M, on_delete=models.CASCADE, default=1)
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


class PHistory3S(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    semestery = models.IntegerField(default=1, null=False, blank=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['ExNo', 'semestery']


class PHistory3SConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(PHistory3S, on_delete=models.CASCADE)


class PHistory3(models.Model):
    PreviosS = models.ForeignKey(PHistory3S, on_delete=models.CASCADE, default=1)
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
