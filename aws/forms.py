from django import forms
from .models import aws
from django.utils.safestring import mark_safe

class aws_QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions')
        super(aws_QuizForm, self).__init__(*args, **kwargs)
        for index, question in enumerate(questions, start=1):
            # 본문과 마지막 문장을 결합 (첫 번째 문장 다음과 마지막 문장 앞에 줄바꿈 추가)
            sentences = question.question_text.split('.')
            if len(sentences) > 1:
                full_question_text = sentences[0] + '.<br>' + '<br>'.join(sentence.strip() for sentence in sentences[1:-1] if sentence.strip())
                if sentences[-1].strip():  # 마지막 문장이 비어있지 않은 경우에만 추가
                    full_question_text += '<br>' + sentences[-1].strip()
            else:
                full_question_text = question.question_text

            if question.question_text_last_line:
                full_question_text += f"<br><br><br>{question.question_text_last_line}"
            
            self.fields[f'question_{question.id}'] = forms.ChoiceField(
                label=mark_safe(f"{index}. {full_question_text}"),
                choices=[
                    ('A', question.option_a),
                    ('B', question.option_b),
                    ('C', question.option_c),
                    ('D', question.option_d)
                ],
                widget=forms.RadioSelect,
                required=False
            )