from django.contrib import admin

from .models import Till, TillClosure


class TillAdmin(admin.ModelAdmin):
    fields = ('name', 'location')

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(TillAdmin, self).save_model(request, obj, form, change)

admin.site.register(Till, TillAdmin)

class TillClosureAdmin(admin.ModelAdmin):
    fields = ['till', 'close_time', 'cash_takings', 'card_takings',
              'total_takings',
              'note_50GBP', 'note_20GBP', 'note_10GBP', 'note_5GBP',
              'coin_2GBP', 'coin_1GBP', 'coin_50p', 'coin_20p',
              'coin_10p', 'coin_5p', 'coin_2p', 'coin_1p',
              'till_total', 'till_float', 'till_difference', 'notes']

    readonly_fields = ['total_takings', 'till_total', 'till_difference']

admin.site.register(TillClosure, TillClosureAdmin)
