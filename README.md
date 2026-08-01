Python Bootcamp – Week 1

هذا المستودع يحتوي على التطبيقات العملية والواجب الخاص بالأسبوع الأول من معسكر تطوير تطبيقات الويب باستخدام لغة Python.

خلال هذا الأسبوع تم تعلم أساسيات التعامل مع سطر الأوامر، إدارة الملفات والمجلدات، كتابة وتشغيل Shell Scripts، استخدام Git وGitHub، وإنشاء البيئات الافتراضية وإدارة مكتبات Python.

Repository Structure
Python-Bootcamp/
│
├── Week-1/
│   └── Labs/
│       ├── Calculator/
│       └── MiniGamesBot/
│
└── Homework-Week-1/
    ├── Cars/
    └── Number-Guessing-Python/
    
Week 1 Topics
Python Basics

تم تعلم عدد من أساسيات لغة Python، ومنها:

كتابة وتشغيل ملفات Python.
استخدام المسافات البادئة Indentation.
التعامل مع المتغيرات والشروط والحلقات.
إنشاء برامج Python بسيطة.
تثبيت واستخدام المكتبات الخارجية.
Linux and Terminal Commands

تم التدرب على مجموعة من أوامر سطر الأوامر، مثل:

pwd
mkdir
touch
cp
mv
rm
cat
head
tail
nano
chmod

تُستخدم هذه الأوامر لإنشاء الملفات والمجلدات، نقلها، نسخها، حذفها، قراءة محتوياتها وتعديل صلاحياتها.

Shell Script Automation

تم إنشاء وتشغيل ملفات Shell Script بصيغة .sh لتنفيذ المهام بشكل تلقائي.

مثال على سكربت لنسخ الملفات إلى مجلد احتياطي:

#!/bin/bash

echo "Starting backup..."

mkdir -p ./Backup
cp -R ./Documents/* ./Backup/

echo "Backup completed."

لجعل السكربت قابلًا للتشغيل:

chmod +x backup.sh

لتشغيل السكربت:

./backup.sh

كما تم التعرف على استخدام:

crontab -e

لجدولة تشغيل السكربت تلقائيًا في وقت محدد.

Python Virtual Environment

تم تعلم كيفية إنشاء وتشغيل وإيقاف البيئة الافتراضية:

python3 -m venv venv
source venv/bin/activate
deactivate

البيئة الافتراضية تساعد على عزل مكتبات كل مشروع عن المشاريع الأخرى.

Python Packages

تم استخدام pip لتثبيت وإدارة مكتبات Python:

pip3 install requests
pip3 list
pip3 freeze > requirements.txt
pip3 install -r requirements.txt
Git and GitHub

تم تعلم أساسيات إدارة إصدارات المشروع باستخدام Git:

git init
git add .
git commit -m "First commit V1"
git status
git log
git log --oneline

كما تم تعلم التعامل مع الفروع:

git switch -c Upgrade
git switch main
git branch
git branch -d Upgrade

ورفع وتحميل المشاريع من GitHub:

git clone <repository-url>
git pull origin main
git push
git push --set-upstream origin Upgrade

Setup

لتحميل المستودع:

git clone https://github.com/AmmarMoha1/Python-bootcamp-tuwaiq.git
cd Python-bootcamp-tuwaiq

لإنشاء البيئة الافتراضية:

python3 -m venv venv
source venv/bin/activate

لتثبيت المكتبات:

pip3 install -r requirements.txt




Python Web Development Bootcamp
