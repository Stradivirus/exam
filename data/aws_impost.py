import os
import sys
import django

# 현재 스크립트의 디렉토리를 얻습니다.
current_dir = os.path.dirname(os.path.abspath(__file__))
# 프로젝트 루트 디렉토리를 Python 경로에 추가
project_root = os.path.dirname(current_dir)
sys.path.append(project_root)

# Django 설정 로드
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exam.settings")
django.setup()

from aws.models import aws

def import_questions_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        questions = content.split('\n\n')
        
        saved_count = 0
        skipped_numbers = []
        
        for index, q in enumerate(questions, start=1):
            lines = q.strip().split('\n')
            if len(lines) == 7:
                question_text = lines[0]  # 첫 번째 줄
                question_text_last_line = lines[1]  # 두 번째 줄
                choices = lines[2:6]
                correct_answer = lines[6].split(':')[-1].strip()
                
                question = aws(
                    question_text=question_text,
                    question_text_last_line=question_text_last_line,
                    option_a=choices[0][3:].strip(),  # "1) " 제거
                    option_b=choices[1][3:].strip(),  # "2) " 제거
                    option_c=choices[2][3:].strip(),  # "3) " 제거
                    option_d=choices[3][3:].strip(),  # "4) " 제거
                    correct_answer=correct_answer
                )
                question.save()
                saved_count += 1
                print(f"저장된 문제 {index}:")
                print(f"본문: {question_text}")
                print(f"마지막 문장: {question_text_last_line}")
            else:
                skipped_numbers.append(index)
                print(f"저장되지 않은 문제 {index}:")
                print(q)
                print("-" * 50)

    print(f"\n문제 가져오기가 완료되었습니다.")
    print(f"저장된 문제 수: {saved_count}")
    print(f"저장되지 않은 문제 번호: {skipped_numbers}")

if __name__ == "__main__":
    # 현재 스크립트와 같은 디렉토리에 있는 Aws1.txt 파일을 사용합니다.
    file_path = os.path.join(current_dir, "Aws1.txt")
    import_questions_from_file(file_path)
