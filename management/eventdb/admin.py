from django.contrib import admin

from .models import Events
from .models import Hosts
from .models import EventHosts
from .models import Registration


admin.site.register(Events)
admin.site.register(Hosts)
admin.site.register(EventHosts)
admin.site.register(Registration)

# Register your models here.
