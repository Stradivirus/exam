#!/bin/bash

# 새 덤프 파일 생성
pg_dump -U moon -h localhost exam > /work/django/exam/linux_db_dump.sql

