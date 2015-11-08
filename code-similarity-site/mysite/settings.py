#coding=utf-8
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import ConfigParser
from os import makedirs
import os
import shutil
import sys
reload(sys)
sys.setdefaultencoding("utf-8")  # @UndefinedVariable



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '052r7m=jisv#7wzfnflak$trhhjfly+#&ls%sr&7-6deggzs#1'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = "*"


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'bootstrap3',
    
    'software_manager',
    'diffHandle',
    'redebug_algorithm',
    'astLevel_algorithm',
    'graph_algorithm',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "mysite/templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'code_similarity',
        'HOST': '211.69.198.89',
        'PORT': '3306',
        'USER': "code_similarity",
        'PASSWORD': "{code}:similarity",
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
#STATIC_ROOT = os.path.join(BASE_DIR, "static")
               
STATIC_URL = '/static/'

STATICFILES_DIRS = [
                    os.path.join(BASE_DIR, "static"),
                    ]
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#session manager
SESSION_EXPIRE_AT_BROWSER_CLOSE=True

# user define variables
conf_file = os.path.join(BASE_DIR, "site.conf")   
conf = ConfigParser.ConfigParser()
conf.read(conf_file)

BASE_PATH = conf.get("path_conf", "file_base_path")
JOERN_PATH = conf.get("path_conf", "joern_path")
NEO4J_HOME = conf.get("path_conf", "neo4j_home")

# BASE_PATH = r"/home/bert/Public/website-files/"
TMP_PATH = os.path.join(BASE_PATH, "TMP")
SOFTWARE_PATH = os.path.join(BASE_PATH, "SOFTWARE")
DIFF_FILE_PATH = os.path.join(BASE_PATH, "DIFF_FILE")
VULN_CODE_PATH = os.path.join(BASE_PATH, "VULN_CODE")
VULN_FUNC_PATH = os.path.join(VULN_CODE_PATH, "VULN_FUNC")
VULN_FUNC_CORE = os.path.join(VULN_CODE_PATH, "VULN_FUNC_CORE")
PATCHED_FUNC_PATH = os.path.join(VULN_CODE_PATH, "PATCHED_FUNC")
NEO4J_DATABASE_PATH = os.path.join(BASE_PATH, "NEO4J_DATABASE")

#邮箱设置
EMAIL_HOST = 'smtp.163.com'                   
EMAIL_PORT = 25                                 
EMAIL_HOST_USER = 'cugNewAir@163.com'       
EMAIL_HOST_PASSWORD = 'songlab2014'                  
EMAIL_SUBJECT_PREFIX = u'[code similarity]'                                       
#The email address that error messages come from,
# such as those sent to ADMINS and MANAGERS.
SERVER_EMAIL = 'cugNewAir@163.com'
ADMINS = (
    ('admin', '371418912@qq.com'),
    ('bertcug', 'bertcug@gmail.com'),
)            

def make_base_dirs():
    if not os.path.isdir(BASE_PATH):
        os.makedirs(BASE_PATH)
    if not os.path.isdir(TMP_PATH):
        os.makedirs(TMP_PATH)
    if not os.path.isdir(SOFTWARE_PATH):
        os.makedirs(SOFTWARE_PATH)
    if not os.path.isdir(DIFF_FILE_PATH):
        os.makedirs(DIFF_FILE_PATH)
    if not os.path.isdir(VULN_FUNC_PATH):
        os, makedirs(VULN_FUNC_PATH)
    if not os.path.isdir(VULN_FUNC_CORE):
        os.makedirs(VULN_FUNC_CORE)
    if not os.path.isdir(PATCHED_FUNC_PATH):
        os.makedirs(PATCHED_FUNC_PATH)
    if not os.path.isdir(NEO4J_DATABASE_PATH):
        os.makedirs(NEO4J_DATABASE_PATH)
        os.makedirs(os.path.join(NEO4J_DATABASE_PATH, "vuln_db", "create_logs"))
    if os.path.isdir(NEO4J_HOME) and not os.path.exists(os.path.join(NEO4J_DATABASE_PATH, "neo4j")):
        shutil.copytree(NEO4J_HOME, os.path.join(NEO4J_DATABASE_PATH, "neo4j"))
        
