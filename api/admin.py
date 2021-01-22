from django.contrib import admin
from .models import empData, empModel, empList
from .models import empData, empModel, leaveModel


admin.site.register(empData)
admin.site.register(empModel)
admin.site.register(empList)
admin.site.register(leaveModel)
