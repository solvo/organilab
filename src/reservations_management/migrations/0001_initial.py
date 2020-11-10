# Generated by Django 2.2.13 on 2020-10-05 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laboratory', '0017_auto_20201005_1241'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReservedProducts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('is_returnable', models.BooleanField(default=True)),
                ('amount_required', models.FloatField()),
                ('initial_date', models.DateTimeField()),
                ('final_date', models.DateTimeField()),
                ('was_returned', models.BooleanField(default=True)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('shelf_object_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratory.ShelfObject')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationTasks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('celery_task_id', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('reserved_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations_management.ReservedProducts')),
            ],
        ),
        migrations.CreateModel(
            name='Reservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(0, 'Processing'), (1, 'Requested'), (2, 'Accepted'), (3, 'Denied'), (4, 'Closed')], default=1)),
                ('comments', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MassiveReservations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(0, 'Processing'), (1, 'Requested'), (2, 'Accepted'), (3, 'Denied'), (4, 'Closed')], default=1)),
                ('comments', models.CharField(max_length=500)),
                ('days', models.SmallIntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday'), (6, 'Sunday')])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]