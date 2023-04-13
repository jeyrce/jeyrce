from django.apps import \
    AppConfig


class CMSConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cms'
    verbose_name = "个人主页"


app_name = "cms"
