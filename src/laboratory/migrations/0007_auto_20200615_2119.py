# Generated by Django 2.2.12 on 2020-06-16 03:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('laboratory', '0006_sustancecharacteristics_precursor_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationUserManagement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group', verbose_name='Group')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(default='', max_length=25, verbose_name='Phone')),
                ('id_card', models.CharField(max_length=100, verbose_name='ID Card')),
                ('laboratories', models.ManyToManyField(blank=True, to='laboratory.Laboratory', verbose_name='Laboratories')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='organizationstructure',
            name='group',
        ),
        migrations.DeleteModel(
            name='PrincipalTechnician',
        ),
        migrations.AddField(
            model_name='organizationusermanagement',
            name='organization',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratory.OrganizationStructure', verbose_name='Organization'),
        ),
        migrations.AddField(
            model_name='organizationusermanagement',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
