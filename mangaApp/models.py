from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Editor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Series(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    cover = models.ImageField(upload_to='covers/')

    def __str__(self):
        return self.title


class Tome(models.Model):
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='tomes/')

    def __str__(self):
        return f"{self.series.title} - Tome {self.number}"


class Chapter(models.Model):
    title = models.CharField(max_length=255)
    number = models.IntegerField()
    series = models.ForeignKey(Series, on_delete=models.CASCADE)
    tome = models.ForeignKey(Tome, on_delete=models.CASCADE)
    file = models.FileField(upload_to='chapters/')

    def __str__(self):
        return f"{self.series.title} - Chapitre {self.number} - {self.title}"
