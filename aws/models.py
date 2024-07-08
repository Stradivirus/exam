from django.db import models

class LastLineBreakTextField(models.TextField):
    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if value:
            lines = value.splitlines()
            if len(lines) > 1:
                lines[-1] = '\n' + lines[-1]
            value = '\n'.join(lines)
            setattr(model_instance, self.attname, value)
        return value

class aws(models.Model):
    question_text = LastLineBreakTextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=100)