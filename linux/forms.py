from django import forms

class AnswerForm(forms.Form):
    def __init__(self, *args, **kwargs):
        num_questions = kwargs.pop('num_questions', 0)
        super(AnswerForm, self).__init__(*args, **kwargs)
        
        for i in range(1, num_questions + 1):
            self.fields[f'question_{i}'] = forms.ChoiceField(
                choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')],
                widget=forms.RadioSelect,
                required=False
            )
