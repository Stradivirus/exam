from django import forms
from .models import aws

class aws_QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(aws_QuizForm, self).__init__(*args, **kwargs)
        for index, question in enumerate(questions, start=1):
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=f"{index}. {question.question_text}",
                choices=[
                    ('A', question.option_a),
                    ('B', question.option_b),
                    ('C', question.option_c),
                    ('D', question.option_d)
                ],
                widget=forms.RadioSelect,
                required=False
            )