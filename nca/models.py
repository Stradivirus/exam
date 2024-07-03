from django.db import models

class NCA(models.Model):
    question_text = models.CharField(max_length=1000)  # 200에서 1000으로 증가
    choice_a = models.CharField(max_length=500)  # 100에서 500으로 증가
    choice_b = models.CharField(max_length=500)
    choice_c = models.CharField(max_length=500)
    choice_d = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=100)  # 이미 충분할 것 같습니다

    def __str__(self):
        return self.question_text
