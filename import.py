import os
import django
import csv

# Django 설정 로드
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exam.settings")
django.setup()

# 모델 임포트
from linux.models import PDF1, PDF2, PDF3, PDF4

def import_data():
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            col1, col2, col3, col4, col5 = map(int, row)
            
            PDF1.objects.create(col1=col1, col2=col2)
            PDF2.objects.create(col1=col1, col3=col3)
            PDF3.objects.create(col1=col1, col4=col4)
            PDF4.objects.create(col1=col1, col5=col5)

    print("데이터가 성공적으로 데이터베이스에 저장되었습니다.")

if __name__ == "__main__":
    import_data()