from django.db import models
from sges import settings
from django.utils._os import safe_join
from weasyprint import default_url_fetcher

# Create your models here.
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, verbose_name="Ultima actualizacion")
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

def get_rol_index(matrix, rol_id):
    i = 0
    for rol in matrix:
        if rol.id == rol_id:
            return i
        else:
            i = i+1
    return -1


def get_rol_at_index(matrix, index):
    i = 0
    for rol in matrix:
        if i == index:
           return  rol
        i = i + 1
    return None



def url_fetcher(url):
    if url.startswith('assets://'):
        url = url[len('assets://'):]
        url = "file://" + safe_join(settings.ASSETS_ROOT, url)
    return default_url_fetcher(url)