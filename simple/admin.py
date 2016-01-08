from django.contrib import admin
from simple.models import A, B


class AAdmin(admin.ModelAdmin):
    readonly_fields = ['b']


class WorkingAAdmin(admin.ModelAdmin):
    readonly_fields = ['working_b']
    def working_b(self, instance):
        return instance.b
    working_b.short_description = 'working'


admin.site.register(A, AAdmin)
#admin.site.register(A, WorkingAAdmin)
admin.site.register(B)