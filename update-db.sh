#!/bin/bash

# 새 덤프 파일 생성
pg_dump -U moon -h localhost linux > /path/to/your/project/linux_db_dump.sql

# 데이터베이스 컨테이너 재시작
docker-compose restart db

# 필요한 경우 데이터베이스 초기화 스크립트 실행
docker-compose exec db psql -U moon -d linux -f /docker-entrypoint-initdb.d/linux_db_dump.sql
