from django.db import models

class Test(models.Model):
    name =models.CharField("Назва Тесту",max_length=150)
    description=models.CharField("Опис ",max_length=2000)
    addDate=models.DateField("Дата додавання",auto_now=True)
    def __str__(self):
        return self.name
class Answer(models.Model):
    name =models.CharField("Заголовок запитання",max_length=150)
    description=models.CharField("Опис ",max_length=2000,null=True)
    Test = models.ForeignKey(Test, on_delete=models.CASCADE)
    point=models.DecimalField("Ціна замовлення",max_digits=3,decimal_places=2,default=1)
    def __str__(self):
        return self.name
class Variants(models.Model):
    name =models.CharField("Заголовок відповіді",max_length=150,null=True)
    is_right=models.BooleanField('Чи є відповідь правильною',null=True)
    Answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    def __str__(self):
        return self.name 