from django.contrib import admin
from .models import PokemonCard, Trainer, Collection

# Display all fields from models including created_at and updated_at
class BaseModelAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'update_at')

class TrainerAdmin(BaseModelAdmin):
    list_display = ('name', 'birthdate', 'location', 'email', 'created_at', 'update_at')

class PokemonCardAdmin(BaseModelAdmin):
    list_display = (
        'name', 'rarity', 'hp', 'card_type', 'attack', 'description', 'weakness',
        'card_number', 'release_date', 'evolution_stage', 'abilities', 'created_at', 'update_at'
    )

class CollectionAdmin(BaseModelAdmin):
    list_display = ('card', 'Trainer', 'collection_date', 'created_at', 'update_at')

# Register your models here.
admin.site.register(PokemonCard, PokemonCardAdmin)
admin.site.register(Trainer, TrainerAdmin)
admin.site.register(Collection, CollectionAdmin)