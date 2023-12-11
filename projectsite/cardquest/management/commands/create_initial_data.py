from django.core.management.base import BaseCommand
from cardquest.models import PokemonCard, Trainer, Collection

class Command (BaseCommand) :
    help = 'Create Initial data for the application'

    def handle(self, *args, **kwargs) :
        self.create_pokemon_cards()
        self.create_trainers()
        self.create_collections()

    def create_pokemon_cards (self) :
        card1 = PokemonCard(name="Pikachu", rarity="Rare",hp=60, card_type="Electric", attack="Thunder Shock",
                    description="A mouse-like pokemon that can generate electricity.",
                    weakness="Ground", card_number=25, release_date="1996-02-27", evolution_stage="Basic",
                    abilities="Static")
        card1.save()

        self.stdout.write(self.style.SUCCESS('Successfuly created Pokemon Cards.'))
        
    # def create_trainers(self) :
    #     pass

    def create_trainers(self) :
        trainer1 = Trainer(name="Ash", birthdate= "1987-05-22",location= "Pallet Town",email= "ash@pokemon.com")
        trainer1.save()

        self.stdout.write(self.style.SUCCESS('Successfuly created Trainers.'))
    
    def create_collections(self):
        card = PokemonCard.objects.first()  
        trainer = Trainer.objects.first() 

        collection1 = Collection(card=card, Trainer=trainer, collection_date="2023-12-11")
        collection1.save()

        self.stdout.write(self.style.SUCCESS('Successfully created Collections.'))

