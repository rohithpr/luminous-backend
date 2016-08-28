from django.db import models

class Location(models.Model):
    left_top = models.CharField(max_length=20)
    resources = models.CharField(max_length=2000)

    def __str__(self):
        return str(self.id) + ' :: ' + str(self.left_top) + ' :: ' + self.resources

class User(models.Model):
    resources = models.CharField(max_length=2000)
    userid = models.CharField(max_length=30)

    def __str__(self):
        return str(self.id) + ' :: ' + str(self.resources) + ' :: ' + self.userid

class LocationUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id) + ' :: ' + str(self.user) + ' : ' + str(self.location)
