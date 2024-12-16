from django.db import models

class Airport(models.Model):
    code = models.CharField(max_length=3)  # Código do aeroporto (ex: LAX, JFK)
    city = models.CharField(max_length=64)  # Nome da cidade

    def __str__(self):
        return f"{self.city} ({self.code})"


class Flight(models.Model):
    origin = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="departures"
    )  # Aeroporto de origem
    destination = models.ForeignKey(
        Airport, on_delete=models.CASCADE, related_name="arrivals"
    )  # Aeroporto de destino
    duration = models.IntegerField()  # Duração do voo em minutos

    def __str__(self):
        return f"{self.origin} to {self.destination}"


class Passenger(models.Model):
    name = models.CharField(max_length=64)  # Nome do passageiro
    flights = models.ManyToManyField(
        Flight, related_name="passengers"
    )  # Relacionamento Many-to-Many com Flight

    def __str__(self):
        return self.name
