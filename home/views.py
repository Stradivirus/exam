from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  # 'index'는 메인 페이지의 URL 이름입니다
        else:
            messages.error(request, '잘못된 사용자 이름 또는 비밀번호입니다.')
    return render(request, 'login.html')
