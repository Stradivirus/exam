from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from .forms import AnswerForm
from .models import PDF1, PDF2, PDF3, PDF4
import os
from django.conf import settings
from django.apps import apps

def pdf_list(request):
    pdf_dir = os.path.join(settings.BASE_DIR, 'pdf')
    pdfs = [f for f in os.listdir(pdf_dir) if f.endswith('.pdf')]
    return render(request, 'pdf_list.html', {'pdfs': pdfs})

def view_pdf(request, filename):
    pdf_path = settings.STATICFILES_DIRS[0] / filename
    if pdf_path.exists():
        pdf_url = settings.STATIC_URL + filename
        num_questions = 100  # 문제 수를 적절히 조정하세요
        form = AnswerForm(num_questions=num_questions)
        return render(request, 'view_pdf.html', {
            'pdf_url': pdf_url,
            'filename': filename,
            'form': form
        })
    else:
        return render(request, 'pdf_not_found.html', {'filename': filename})

def result(request, filename):
    if request.method == 'POST':
        num_questions = 100  # 문제 수를 적절히 조정하세요
        form = AnswerForm(request.POST, num_questions=num_questions)
        if form.is_valid():
            user_answers = {f"question_{i}": int(form.cleaned_data[f'question_{i}']) 
                            for i in range(1, num_questions + 1) 
                            if form.cleaned_data[f'question_{i}']}
            
            # 파일 이름에 따라 적절한 모델 선택
            pdf_number = filename.split('.')[0][-1]  # 파일 이름에서 숫자 추출
            model_name = f'PDF{pdf_number}'
            model = apps.get_model('linux', model_name)
            
            # 데이터베이스에서 정답 불러오기
            correct_answers = {f"question_{answer.col1}": getattr(answer, f'col{int(pdf_number) + 1}') 
                               for answer in model.objects.all()}
            
            results = []
            score = 0
            for q, user_ans in user_answers.items():
                question_number = int(q.split('_')[1])
                correct_ans = correct_answers.get(q)
                if correct_ans is None:
                    continue  # 데이터베이스에 해당 문제의 정답이 없는 경우 스킵
                is_correct = user_ans == correct_ans
                if is_correct:
                    score += 1
                results.append({
                    'question': question_number,
                    'user_answer': user_ans,
                    'correct_answer': correct_ans,
                    'is_correct': is_correct
                })
            
            total_questions = len(results)
            percentage = (score / total_questions) * 100 if total_questions > 0 else 0

            return render(request, 'result.html', {
                'results': results,
                'score': score,
                'total_questions': total_questions,
                'percentage': round(percentage, 2),
                'filename': filename
            })
        else:
            # 폼이 유효하지 않은 경우, 에러 메시지와 함께 다시 폼을 보여줍니다.
            pdf_url = settings.STATIC_URL + filename
            return render(request, 'view_pdf.html', {
                'pdf_url': pdf_url,
                'filename': filename,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(['POST'])