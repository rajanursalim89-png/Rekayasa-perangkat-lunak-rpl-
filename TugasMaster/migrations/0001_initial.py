from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mahasiswa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=100)),
                ('nim', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('kelas', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tugas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=150)),
                ('mata_kuliah', models.CharField(max_length=100)),
                ('deadline', models.DateField()),
                ('status', models.CharField(choices=[('Dibuka', 'Dibuka'), ('Ditutup', 'Ditutup')], default='Dibuka', max_length=10)),
            ],
        ),
    ]
