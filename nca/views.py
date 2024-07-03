from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
from .models import NCA
from .forms import QuizForm

def quiz(request):
    questions = list(NCA.objects.all())
    total_questions = len(questions)
    num_questions = min(30, total_questions)

    if request.method == 'POST':
        selected_question_ids = request.session.get('selected_question_ids', [])
        selected_questions = NCA.objects.filter(id__in=selected_question_ids)
        form = QuizForm(request.POST, questions=selected_questions)
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
            return HttpResponseRedirect(f"{reverse('result_view')}?score={score}&total={num_questions}")
    else:
        selected_questions = random.sample(questions, num_questions)
        request.session['selected_question_ids'] = [q.id for q in selected_questions]
        form = QuizForm(questions=selected_questions)
    
    return render(request, 'nca/quiz.html', {'form': form, 'total_questions': total_questions})

def result_view(request):
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

def import_questions(request):
    if request.method == 'POST':
        form = QuestionImportForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            questions = file.read().decode('utf-8').split('\n\n')
            for q in questions:
                lines = q.strip().split('\n')
                if len(lines) == 6:
                    question_text = lines[0]
                    choices = lines[1:5]
                    correct_answer = lines[5].split(':')[-1].strip()
                    
                    question = Question(
                        question_text=question_text,
                        choice_a=choices[0][3:].strip(),
                        choice_b=choices[1][3:].strip(),
                        choice_c=choices[2][3:].strip(),
                        choice_d=choices[3][3:].strip(),
                        correct_answer=correct_answer
                    )
                    question.save()
            return render(request, 'nca/import_success.html')
    else:
        form = QuestionImportForm()
    return render(request, 'nca/import.html', {'form': form})

def quiz_view(request):
    if request.method == 'POST':
        form = QuizForm(request.POST, questions=Question.objects.all())
        if form.is_valid():
            return redirect('result')
    else:
        form = QuizForm(questions=Question.objects.all())

    return render(request, 'quiz.html', {'form': form})


