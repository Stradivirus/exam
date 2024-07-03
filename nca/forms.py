from django import forms
from .models import NCA

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(QuizForm, self).__init__(*args, **kwargs)
        for index, question in enumerate(questions, start=1):
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=f"{index}. {question.question_text}",
                choices=[
                    (question.choice_a, question.choice_a),
                    (question.choice_b, question.choice_b),
                    (question.choice_c, question.choice_c),
                    (question.choice_d, question.choice_d)
                ],
                widget=forms.RadioSelect,
                required=False
            )


