from django.db import models

from manager.models import Student


# Create your models here.

class NewPMarwan(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='NewP/Marwan')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class NewPMarwanConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(NewPMarwan, on_delete=models.CASCADE)


class NewPRasha(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='NewP/Rasha')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class NewPRashaConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(NewPRasha, on_delete=models.CASCADE)


class NewPRawa(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='NewP/Rawa')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class NewPRawaConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(NewPRawa, on_delete=models.CASCADE)


class GNewP(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='NewP/GNewP')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class PNewP(models.Model):
    pyear = models.IntegerField(default=0, null=False)
    lfile = models.FileField(upload_to='NewP/PNewP')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['pyear', 'number']


class PNewPConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(PNewP, on_delete=models.CASCADE)


# ---------------------------NewC-----------------------------------------
class NewCMhmd(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='NewC/Mhmd')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class NewCMhmdConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(NewCMhmd, on_delete=models.CASCADE)


class NewCAhmd(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='NewC/Ahmd')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class NewCAhmdConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(NewCAhmd, on_delete=models.CASCADE)


class GNewC(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='NewC/GNewC')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class PNewC(models.Model):
    pyear = models.IntegerField(default=0, null=False)
    lfile = models.FileField(upload_to='NewC/PNewC')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['pyear', 'number']


class PNewCConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(PNewC, on_delete=models.CASCADE)


# -------------------------------------NewI--------------------------------------------

class NewIAhmd(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='NewI/Ahmd')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class NewIAhmdConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(NewIAhmd, on_delete=models.CASCADE)


class NewISamy(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='NewI/Samy')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class NewISamyConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(NewISamy, on_delete=models.CASCADE)


class NewIWfaa(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='NewI/Wfaa')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class NewIWfaaConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(NewIWfaa, on_delete=models.CASCADE)


class GNewI(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='NewI/GNewI')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class PNewI(models.Model):
    pyear = models.IntegerField(default=0, null=False)
    lfile = models.FileField(upload_to='NewI/PNewI')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['pyear', 'number']


class PNewIConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(PNewI, on_delete=models.CASCADE)


# --------------------------------Studes-------------------------------
class SAGrammer51(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='SGMA/SAGrammer1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class SAGrammer51Connent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(SAGrammer51, on_delete=models.CASCADE)


class SAGrammar54M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)


class SAGrammar54MConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(SAGrammar54M, on_delete=models.CASCADE)


class SAGrammer54(models.Model):
    ExNo = models.ForeignKey(SAGrammar54M, on_delete=models.CASCADE, default=1)
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


class SAMorphology51(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='SGMA/SAMorphology1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')


class SAMorphology51Connent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(SAMorphology51, on_delete=models.CASCADE)


class SAMorphology54M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering = ['number']


class SAMorphology54MConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(SAMorphology54M, on_delete=models.CASCADE)


class SAMorphology54(models.Model):
    ExNo = models.ForeignKey(SAMorphology54M, on_delete=models.CASCADE, default=1)
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


class SAGMA5GoldenM(models.Model):
    name = models.TextField(max_length=100, null=False, default="0")
    publish = models.BooleanField()
    lprice = models.IntegerField(default=1)


class SAGMA5Golden(models.Model):
    ExNo = models.ForeignKey(SAGMA5GoldenM, on_delete=models.CASCADE, default=1)
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


class SAGMA5PriveosS(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    semestery = models.IntegerField(default=1, null=False, blank=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['ExNo', 'semestery']


class SAGMA5PriveosSConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(SAGMA5PriveosS, on_delete=models.CASCADE)


class SAGMA5Priveos(models.Model):
    PreviosS = models.ForeignKey(SAGMA5PriveosS, on_delete=models.CASCADE, default=1)
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


# --------------------------------MUMluke-------------------------------
class MAGrammer51(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='MGMA/MAGrammer1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class MAGrammer51Connent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(MAGrammer51, on_delete=models.CASCADE)


class MAGrammar54M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)


class MAGrammar54MConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(MAGrammar54M, on_delete=models.CASCADE)


class MAGrammer54(models.Model):
    ExNo = models.ForeignKey(MAGrammar54M, on_delete=models.CASCADE, default=1)
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


class MAMorphology51(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='MGMA/MAMorphology1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')


class MAMorphology51Connent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(MAMorphology51, on_delete=models.CASCADE)


class MAMorphology54M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering = ['number']


class MAMorphology54MConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(MAMorphology54M, on_delete=models.CASCADE)


class MAMorphology54(models.Model):
    ExNo = models.ForeignKey(MAMorphology54M, on_delete=models.CASCADE, default=1)
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


class MANathr51(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='MGMA/MANathr51')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class MANathr51Connent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(MANathr51, on_delete=models.CASCADE)


class MANathr54M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)


class MANathr54MConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(MANathr54M, on_delete=models.CASCADE)


class MANathr54(models.Model):
    ExNo = models.ForeignKey(MANathr54M, on_delete=models.CASCADE, default=1)
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


class MAGMA5GoldenM(models.Model):
    name = models.TextField(max_length=100, null=False, default="0")
    publish = models.BooleanField()
    lprice = models.IntegerField(default=1)


class MAGMA5Golden(models.Model):
    ExNo = models.ForeignKey(MAGMA5GoldenM, on_delete=models.CASCADE, default=1)
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


class MAGMA5PriveosS(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    semestery = models.IntegerField(default=1, null=False, blank=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['ExNo', 'semestery']


class MAGMA5PriveosSConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(MAGMA5PriveosS, on_delete=models.CASCADE)


class MAGMA5Priveos(models.Model):
    PreviosS = models.ForeignKey(MAGMA5PriveosS, on_delete=models.CASCADE, default=1)
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


# ---------------History4--------------------------------------------------------

class History41(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='History4/History41')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')


class History41Connent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(History41, on_delete=models.CASCADE)


class History44M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering = ['number']


class History44MConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(History44M, on_delete=models.CASCADE)


class History44(models.Model):
    ExNo = models.ForeignKey(History44M, on_delete=models.CASCADE, default=1)
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


class GHistory4M(models.Model):
    name = models.TextField(max_length=100, null=False, default="0")
    publish = models.BooleanField()
    lprice = models.IntegerField(default=1)


class GHistory4(models.Model):
    ExNo = models.ForeignKey(GHistory4M, on_delete=models.CASCADE, default=1)
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


class PHistory4S(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    semestery = models.IntegerField(default=1, null=False, blank=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['ExNo', 'semestery']


class PHistory4SConnent(models.Model):
    user = models.ForeignKey(Student, on_delete=models.CASCADE)
    lecture = models.ForeignKey(PHistory4S, on_delete=models.CASCADE)


class PHistory4(models.Model):
    PreviosS = models.ForeignKey(PHistory4S, on_delete=models.CASCADE, default=1)
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
