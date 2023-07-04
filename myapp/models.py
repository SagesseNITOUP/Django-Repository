from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=20)
    statut = models.BooleanField(default=False)

    class Meta:
        db_table = "users"



class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    categorie = models.CharField(max_length=15)
    quantite = models.PositiveIntegerField()
    statut = models.BooleanField(default=False)

    class Meta : 
        db_table = "produits"
