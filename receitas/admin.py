from django.contrib import admin
#from django.contrib.auth.models import Group
#from .models import Snippet
from .models import Prescricao, Remedio

#admin.site.unregister(Group)
admin.site.register(Prescricao)
admin.site.register(Remedio)
