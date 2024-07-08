from django.db import models

class LastLineBreakTextField(models.TextField):
    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname)
        if value:
            lines = value.splitlines()
            if len(lines) > 1:
                last_line = lines.pop()
                setattr(model_instance, f'{self.attname}_last_line', last_line)
                value = '\n'.join(lines)
            setattr(model_instance, self.attname, value)
        return value

class aws(models.Model):
    question_text = LastLineBreakTextField()
    question_text_last_line = models.TextField(blank=True)
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=100)
