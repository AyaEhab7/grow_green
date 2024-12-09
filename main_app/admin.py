from django.contrib import admin
from .models import Nurseries, Plants, Irrigation, Fertilization, PestControl

admin.site.register(Nurseries)
admin.site.register(Plants)
admin.site.register(Irrigation)
admin.site.register(Fertilization)
admin.site.register(PestControl)

