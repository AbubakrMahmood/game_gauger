from django.contrib import admin

from .models import Game, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('game', 'rating', 'user_name', 'comment', 'comment_date')
    list_filter = ['comment_date', 'user_name']
    search_fields = ['comment']

class GameAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('game',)}
    
admin.site.register(Game,GameAdmin)
admin.site.register(Review, ReviewAdmin)
