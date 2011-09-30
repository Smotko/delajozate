from django.contrib import admin
from delajozate.dz.models import Oseba, Stranka, Skupina, ClanStranke, \
	Mandat, Poslanec, Odbor, ClanOdbora

class PoslanecAdmin(admin.ModelAdmin):
	list_display = ('oseba', 'mandat', 'od', 'do')
	list_filter = ('mandat',)

class StrankaAdmin(admin.ModelAdmin):
	list_display = ('ime', 'okrajsava', 'od', 'do')

admin.site.register(Oseba)
admin.site.register(Stranka, StrankaAdmin)
admin.site.register(Skupina)
admin.site.register(ClanStranke)
admin.site.register(Mandat)
admin.site.register(Poslanec, PoslanecAdmin)
admin.site.register(Odbor)
admin.site.register(ClanOdbora)


