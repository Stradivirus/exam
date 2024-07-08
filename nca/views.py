from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
from .models import NCA
from .forms import nca_QuizForm

def nca_quiz(request):
    questions = list(NCA.objects.all())
    total_questions = len(questions)
    num_questions = min(30, total_questions)

    if request.method == 'POST':
        selected_question_ids = request.session.get('selected_question_ids', [])
        selected_questions = NCA.objects.filter(id__in=selected_question_ids)
        form = nca_QuizForm(request.POST, questions=selected_questions)
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
                    'choices': {
                        'A': question.choice_a,
                        'B': question.choice_b,
                        'C': question.choice_c,
                        'D': question.choice_d,
                    },
                    'user_answer': answer,
                    'correct_answer': question.correct_answer,
                    'is_correct': is_correct
                })
            request.session['quiz_results'] = results
            return HttpResponseRedirect(f"{reverse('nca_result_view')}?score={score}&total={num_questions}")
    else:
        selected_questions = random.sample(questions, num_questions)
        request.session['selected_question_ids'] = [q.id for q in selected_questions]
        form = nca_QuizForm(questions=selected_questions)
    
    return render(request, 'nca/quiz.html', {'form': form, 'total_questions': total_questions})

def nca_result_view(request):
    score = request.GET.get('score', 0)
    total = request.GET.get('total', 0)
    results = request.session.get('quiz_results', [])
    selected_question_ids = request.session.get('selected_question_ids', [])
    selected_questions = NCA.objects.filter(id__in=selected_question_ids)
    
    for result, question in zip(results, selected_questions):
        result['question_text'] = question.question_text
        result['choices'] = {
            'A': question.choice_a,
            'B': question.choice_b,
            'C': question.choice_c,
            'D': question.choice_d,
        }
    
    return render(request, 'nca/result.html', {'score': score, 'total': total, 'results': results})
