from django.contrib import admin

from .models import Retreat, Booking

# To visualize it on admin page
class RetreatAdmin(admin.ModelAdmin):
    list_display = ('id','date', 'title', 'description', 'date', 'location', 'price', 'type', 'condition', 'image', 'duration')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'retreat', 'user', 'payment_detail')

admin.site.register(Retreat, RetreatAdmin)
admin.site.register(Booking, BookingAdmin)
