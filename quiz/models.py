from django.db import models
from django.utils.translation import gettext_lazy as _



class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Quizes(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Quizes"

    def __str__(self):
        return self.title
    


class Question(models.Model):
    SCALE = (
       (0, _("Fundamental")),
       (1, _("Beginner")),
       (2, _("Intermediate")),
       (3, _("Advance")),
       (4, _("Expert")),
    )

    TYPE = (
        (0, _("Multiple Choices")),
    )

    quiz = models.ForeignKey(Quizes, related_name="question", on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, default=0, verbose_name=_("Type of Question"))
    title = models.CharField(max_length=200, verbose_name=_("Title"))
    difficulty = models.IntegerField(choices=SCALE, default=0, verbose_name=_("Difficulty"))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    date_updated = models.DateTimeField(auto_now=True, verbose_name=_("Date Updated"))
    status = models.BooleanField(default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answer", on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=200, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False, verbose_name=_("Is Right"))

    def __str__(self):
        return self.answer_text