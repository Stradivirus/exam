from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
from .models import aws
from .forms import aws_QuizForm

def aws_quiz(request):
    questions = list(aws.objects.all())
    total_questions = len(questions)
    num_questions = min(40, total_questions)
    if request.method == 'POST':
        selected_question_ids = request.session.get('selected_question_ids', [])
        selected_questions = aws.objects.filter(id__in=selected_question_ids)
        form = aws_QuizForm(request.POST, questions=selected_questions)
        if form.is_valid():
            score = 0
            results = []
            for question in selected_questions:
                answer = form.cleaned_data[f'question_{question.id}']
                is_correct = answer == question.correct_answer
                if is_correct:
                    score += 1
                results.append({
                    'question_id': question.id,
                    'question_text': question.question_text,
                    'question_text_last_line': question.question_text_last_line,  # 추가된 부분
                    'choices': {
                        'A': question.option_a,
                        'B': question.option_b,
                        'C': question.option_c,
                        'D': question.option_d,
                    },
                    'user_answer': answer,
                    'correct_answer': question.correct_answer,
                    'is_correct': is_correct
                })
            request.session['quiz_results'] = results
            return HttpResponseRedirect(f"{reverse('aws_result_view')}?score={score}&total={num_questions}")
    else:
        selected_questions = random.sample(questions, num_questions)
        request.session['selected_question_ids'] = [q.id for q in selected_questions]
        form = aws_QuizForm(questions=selected_questions)
   
    return render(request, 'aws/quiz.html', {'form': form, 'total_questions': total_questions})

def aws_result_view(request):
    score = request.GET.get('score', 0)
    total = request.GET.get('total', 0)
    results = request.session.get('quiz_results', [])
    selected_question_ids = request.session.get('selected_question_ids', [])
    selected_questions = aws.objects.filter(id__in=selected_question_ids)
    
    for result, question in zip(results, selected_questions):
        result['question_text'] = question.question_text
        result['choices'] = {
            'A': question.option_a,
            'B': question.option_b,
            'C': question.option_c,
            'D': question.option_d,
        }
    
    return render(request, 'aws/result.html', {'score': score, 'total': total, 'results': results})
