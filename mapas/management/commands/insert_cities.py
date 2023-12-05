from django.db import transaction
from django.core.management.base import BaseCommand
from mapas.models import City
import csv, os

class Command(BaseCommand):
    
    """
    Django management command to import cities from a CSV file.

    Usage:
    python manage.py insert_cities cities.csv
    """
    
    help = "Import cities from a CSV file"

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file')

    def handle(self, *args, **kwargs):
        
        """
        Handle method for executing the command.
        """
        
        current_directory = os.path.dirname(os.path.abspath(__file__))
        csv_path = os.path.join(current_directory, 'cities.csv')

        if os.path.exists(csv_path):
            with open(csv_path, "r", encoding='utf-8') as file:
                reader = csv.reader(file)
                
                for row in reader:
                    city, state, country = row
                    print(f"City: {city}, State: {state}, Country: {country}")  # Verifica los datos
                    
                    try:
                        City.objects.create(name=city, state=state, country=country)
                        self.stdout.write(self.style.SUCCESS(f"Successfully created city: {city}"))
                    except Exception as e:
                        self.stdout.write(self.style.ERROR(f"Error creating city {city}: {e}"))
            
            self.stdout.write(self.style.SUCCESS("Successfully imported cities"))
        else:
            self.stdout.write(self.style.ERROR("File cities.csv not found in the expected directory"))
