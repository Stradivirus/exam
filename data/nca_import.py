import os
import django

# Django 설정 로드
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exam.settings")
django.setup()

from nca.models import NCA

def import_questions_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        questions = content.split('\n\n')
        
        saved_count = 0
        skipped_count = 0
        
        for index, q in enumerate(questions, start=1):
            lines = q.strip().split('\n')
            if len(lines) == 6:
                question_text = lines[0]
                choices = lines[1:5]
                correct_answer = lines[5].split(':')[-1].strip()
                
                question = NCA(
                    question_text=question_text,
                    choice_a=choices[0][3:].strip(),  # "1) " 제거
                    choice_b=choices[1][3:].strip(),  # "2) " 제거
                    choice_c=choices[2][3:].strip(),  # "3) " 제거
                    choice_d=choices[3][3:].strip(),  # "4) " 제거
                    correct_answer=correct_answer
                )
                question.save()
                saved_count += 1
                print(f"저장된 문제 {index}: {question_text}")
            else:
                skipped_count += 1
                print(f"저장되지 않은 문제 {index}:")
                print(q)
                print("-" * 50)

    print(f"\n문제 가져오기가 완료되었습니다.")
    print(f"저장된 문제 수: {saved_count}")
    print(f"저장되지 않은 문제 수: {skipped_count}")

if __name__ == "__main__":
    file_path = "/work/django/exam/nca.txt"  # 실제 txt 파일 경로로 변경하세요
    import_questions_from_file(file_path)
