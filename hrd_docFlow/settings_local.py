"""
Django settings for hrd_docFlow project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path
# import ldap
# from django_auth_ldap.config import *

os.sep = "/"
os.path.sep = "/"
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'g*307m7rj^^kc-#5+)8gutkt-@bv#tt&)*u_=!y2c(9t*1iw+a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Baseline LDAP configuration.
# AUTH_LDAP_SERVER_URI = "ldap://172.16.8.10"
# AUTH_LDAP_AUTHORIZE_ALL_USERS = True
# AUTH_LDAP_PERMIT_EMPTY_PASSWORD = True
#
# # Логин пользователя от чьего имени будут выполнятся запросы к LDAP (кроме авторизации)
# #AUTH_LDAP_BIND_DN = "cn=bot_hrd_ldap_auth,dc=pvk,dc=local"
# AUTH_LDAP_BIND_DN = "PVK\\bot_hrd_ldap_auth"
# AUTH_LDAP_BIND_PASSWORD = "8542c90c498256cb5965e203107c1319"
#
# # Настройка будет пытаться найти пользователя в созданной нами OU Django и стандартной папке Users,
# # сопоставляя введенный login пользователя с аттрибутами sAMAccountName
# AUTH_LDAP_USER_SEARCH = LDAPSearchUnion(
#         LDAPSearch("dc=pvk,dc=local", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"),
#         LDAPSearch("dc=pvk,dc=local", ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)"),
# )
#
# # Set up the basic group parameters.
# AUTH_LDAP_GROUP_SEARCH = LDAPSearch("dc=pvk,dc=local",
#     ldap.SCOPE_SUBTREE, "(objectClass=group)"
# )
# AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")
#
# # Simple group restrictions
# # AUTH_LDAP_REQUIRE_GROUP - если определено DN для этой настройки, то требуется присутсвие пользователя в этой группе
# # в противном случае пользовталю будет отказано в аутентификации
# # таким образом указываем, что для того чтобы пользователь был аутентифицирован он обязан находится в группе "active"
# # AUTH_LDAP_REQUIRE_GROUP = "dc=pvk,dc=local"
#
# # AUTH_LDAP_DENY_GROUP - если определено DN для этой настройки, то в случае члентсва пользователя в этой группе
# # ему будет отказано в аутентификации
# # AUTH_LDAP_DENY_GROUP = "cn=disabled,ou=Groups,ou=Django,dc=company,dc=ru"
#
# # Populate the Django user from the LDAP directory.
# # Указываем как переносить данные из AD в стандартный профиль пользователя Django
# AUTH_LDAP_USER_ATTR_MAP = {
#     "username": "sAMAccountName",
#     "first_name": "cn",
#     "email": "mail"
# }
# # Указываем как переносить данные из AD в расширенный профиль пользователя Django
# AUTH_LDAP_PROFILE_ATTR_MAP = {
#     "employee_number": "employeeNumber"
# }
#
# # Указываем привязку стандартных флагов is_active, is_staff и is_superuser к членству в группах AD
# # Флаг is_active при использовании django_remote_auth_ldap сам по себе не оказывает вляния на разрешение аутнтификации
# # поэтому для создания обычного поведения Django также определяме настройку AUTH_LDAP_REQUIRE_GROUP (см.выше)
# AUTH_LDAP_USER_FLAGS_BY_GROUP = {
#     "is_active": "dc=pvk,dc=local",
#     "is_staff": "ou=core,dc=pvk,dc=local",
#     # "is_superuser": "cn=superuser,ou=Groups,ou=Django,dc=company,dc=ru"
# }
#
# # Указываем привязку флагов расширенного профиля к членству в группах AD
# # AUTH_LDAP_PROFILE_FLAGS_BY_GROUP = {
# #     "is_awesome": "cn=awesome,ou=Groups,ou=Django,dc=company,dc=ru",
# # }
#
# # This is the default, but I like to be explicit.
# AUTH_LDAP_ALWAYS_UPDATE_USER = False
#
# # Use LDAP group membership to calculate group permissions.
# # AUTH_LDAP_FIND_GROUP_PERMS = True
#
# # Cache group memberships for an hour to minimize LDAP traffic
# AUTH_LDAP_CACHE_GROUPS = True
# AUTH_LDAP_GROUP_CACHE_TIMEOUT = 3600


AUTHENTICATION_BACKENDS = (
    # 'django_remote_auth_ldap.backend.RemoteUserLDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
     # 'django_auth_ldap.backend.LDAPBackend',
)


# Application definition

INSTALLED_APPS = [
'vac_shed',
        'shift_shed',
    'TURV',
    'reg_jounals',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

ROOT_URLCONF = 'hrd_docFlow.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        # 'DIRS': [BASE_DIR, 'templates'],
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

WSGI_APPLICATION = 'hrd_docFlow.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
#         }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hrd_docflow_test',
        'USER': 'hrd_user',
        'PASSWORD': 'hrdpassword',
        'HOST': '172.16.23.38',
        # 'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}







# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]

# Redirect to home URL after login (Default redirects to /accounts/profile/)
LOGIN_REDIRECT_URL = '/'


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Asia/Kamchatka'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
    

]
