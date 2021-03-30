from django.db import models

# Create your models here.


# Create your models here.
class Musician(models.Model):
    # id = models.AutoField(Primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name


class Album(models.Model):
    # id = models.AutoField(Primary_key=True)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    # rating = (
    # (1, "Worst"),
    # (2, "Bad"),
    # (3, "Not Bad"),
    # (4, "Good"),
    # (5, "Excellent!"),
    # )

    rating = (
        ( "Worst",1),
        ( "Bad",2),
        ( "Not Bad",3),
        ( "Good",4),
        ( "Excellent!",5),
        )
    num_stars = models.CharField(choices=rating,max_length=30)

    def __str__(self):
        return self.name + ", Rating: " + str(self.num_stars)
