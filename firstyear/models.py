from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(null=False, max_length=50, unique=True)
    password = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.username


class FirstYearsUser(models.Model):
    username = models.CharField(null=False, max_length=50, unique=True)
    password = models.CharField(null=False, max_length=50)

    def __str__(self):
        return self.username


class WGrammar(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA/WGrammar')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)


class WMorphology(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA/WMorphology')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')

    class Meta:
        ordering = ['number']


class WGMAGlden(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA/WGMAGlden')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class WGMAPriveos(models.Model):
    pyear = models.IntegerField(default=0, null=False)
    lfile = models.FileField(upload_to='GMA/WGMAPriveos')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['pyear', 'number']


class AGrammer1(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA/AGrammer1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(default=1, null=False)
    publish = models.BooleanField(null=True, default=True)


class AGrammar4M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)


class AGrammer4(models.Model):
    ExNo = models.ForeignKey(AGrammar4M, on_delete=models.CASCADE, default=1)
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


class AMorphology1(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA/AMorphology1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')


class AMorphology4M(models.Model):
    name = models.CharField(max_length=55, null=False)
    number = models.IntegerField(default=1, null=False, blank=False)
    publish = models.BooleanField(null=True, default=True)
    lprice = models.IntegerField(default=1, null=True, blank=True)

    class Meta:
        ordering = ['number']


class AMorphology4(models.Model):
    ExNo = models.ForeignKey(AMorphology4M, on_delete=models.CASCADE, default=1)
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


class AGMAGoldenM(models.Model):
    name = models.TextField(max_length=100,null=False,default="0")
    publish = models.BooleanField()
    lprice = models.IntegerField(default=1)



class AGMAGolden(models.Model):
    ExNo = models.ForeignKey(AGMAGoldenM, on_delete=models.CASCADE, default=1)
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


class AGMAPriveosS(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    semestery = models.IntegerField(default=1, null=False, blank=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['ExNo', 'semestery']


class AGMAPriveos(models.Model):
    PreviosS = models.ForeignKey(AGMAPriveosS, on_delete=models.CASCADE, default=1)
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


class Application1(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA/Application1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class Application2(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA/Application2')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class Application3(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA/Application3')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class Application4(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA/Application4')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class Application5(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='GMA/Application5')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class ApplicationExM(models.Model):
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class ApplicationEx1(models.Model):
    ExNo=models.ForeignKey(ApplicationExM, on_delete=models.CASCADE, default=0)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False,unique=True)


    class Meta:
        ordering = ['number']


class ApplicationEx2(models.Model):
    ExNo=models.ForeignKey(ApplicationExM, on_delete=models.CASCADE, default=0)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False,unique=True)


    class Meta:
        ordering = ['number']


class ApplicationEx3(models.Model):
    ExNo=models.ForeignKey(ApplicationExM, on_delete=models.CASCADE, default=0)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False,unique=True)


    class Meta:
        ordering = ['number']


class ApplicationEx4(models.Model):
    ExNo=models.ForeignKey(ApplicationExM, on_delete=models.CASCADE, default=0)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False,unique=True)


    class Meta:
        ordering = ['number']


class ApplicationEx5(models.Model):
    ExNo=models.ForeignKey(ApplicationExM, on_delete=models.CASCADE, default=0)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False,unique=True)


    class Meta:
        ordering = ['number']


class ApplicationEx6(models.Model):
    ExNo=models.ForeignKey(ApplicationExM, on_delete=models.CASCADE, default=0)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False,unique=True)


    class Meta:
        ordering = ['number']


class WResearchSeedsL(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='ResearchSeeds/L')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')

    class Meta:
        ordering = ['number']


class WResearchSeedsG(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='ResearchSeeds/G')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')

    class Meta:
        ordering = ['number']


class WResearchSeedsP(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='ResearchSeeds/P')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')

    class Meta:
        ordering = ['number']


class AResearchSeeds1(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='ResearchSeeds/A1')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)
    number = models.IntegerField(null=False, default='1')


class AResearchSeeds4(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['number']


class AResearchSeedsG(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['number']


class AResearchSeedsP(models.Model):
    ExNo = models.IntegerField(default=1, null=False, blank=False)
    question = models.TextField(null=False)
    ans1 = models.TextField(null=False)
    ans2 = models.TextField(null=False)
    ans3 = models.TextField(null=False)
    ans4 = models.TextField(null=False)
    why = models.TextField(default='')
    No_true = models.IntegerField(default=1, null=False)
    number = models.IntegerField(default=1, null=False)
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)

    class Meta:
        ordering = ['number']


class APre_IslamicLiterature(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Pre_IslamicLiterature/A')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)


class HPre_IslamicLiterature(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Pre_IslamicLiterature/A')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)


class GPre_IslamicLiterature(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Pre_IslamicLiterature/G')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    publish = models.BooleanField(null=True, default=True)


class PPre_IslamicLiterature(models.Model):
    lname = models.CharField(max_length=55, null=False)
    lfile = models.FileField(upload_to='Pre_IslamicLiterature/P')
    lprice = models.IntegerField(default=0, null=True, blank=True)
    number = models.IntegerField(null=False, default='1')
    publish = models.BooleanField(null=True, default=True)