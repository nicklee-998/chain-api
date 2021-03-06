from django.contrib import admin
from chain.core.models import (Site, Device, Unit, Metric, Sensor,
                                 ScalarData, Person, GeoLocation)


admin.site.register(GeoLocation)
admin.site.register(Site)
admin.site.register(Device)
admin.site.register(ScalarData)
admin.site.register(Sensor)
admin.site.register(Unit)
admin.site.register(Metric)
admin.site.register(Person)
