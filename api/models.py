from django.db import models
from django.core.exceptions import ValidationError

class Voter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    has_voted = models.BooleanField(default=False)

    def clean(self):
        if Candidate.objects.filter(email=self.email).exists():
            raise ValidationError("Este correo ya está registrado como candidato.")

    def __str__(self):
        return self.name

class Candidate(models.Model):
    name = models.CharField(max_length=100)
    party = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    votes = models.PositiveIntegerField(default=0)

    def clean(self):
        if Voter.objects.filter(email=self.email).exists():
            raise ValidationError("Este correo ya está registrado como votante.")

    def __str__(self):
        return self.name

class Vote(models.Model):
    voter = models.OneToOneField(Voter, on_delete=models.CASCADE) 
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if self.voter.has_voted:
            raise ValidationError("El votante ya ha emitido su voto.")
        self.voter.has_voted = True
        self.voter.save()
        self.candidate.votes += 1
        self.candidate.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.voter.name} votó por {self.candidate.name}"
