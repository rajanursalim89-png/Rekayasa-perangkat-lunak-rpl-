from django.db import models


class Mahasiswa(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=20)
    email = models.EmailField()
    kelas = models.CharField(max_length=50)

    def __str__(self):
        return self.nama


class Tugas(models.Model):
    STATUS_CHOICES = [
        ('Dibuka', 'Dibuka'),
        ('Ditutup', 'Ditutup'),
    ]

    judul = models.CharField(max_length=150)
    mata_kuliah = models.CharField(max_length=100)
    deadline = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Dibuka')

    def __str__(self):
        return self.judul
