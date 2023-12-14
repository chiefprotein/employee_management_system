from django.contrib import admin

# Register your models here.


from .models import emp

admin.site.register(emp)


from .models import manager

admin.site.register(manager)

from .models import login

admin.site.register(login)


