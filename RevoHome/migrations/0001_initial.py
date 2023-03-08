# Generated by Django 4.1.7 on 2023-03-08 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Build',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BuildSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='BuildPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('length', models.FloatField(blank=True, null=True)),
                ('quantity', models.PositiveIntegerField()),
                ('build', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parts', to='RevoHome.build')),
            ],
        ),
        migrations.AddField(
            model_name='build',
            name='build_section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RevoHome.buildsection'),
        ),
        migrations.CreateModel(
            name='AmountMade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_made', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('build_section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amounts', to='RevoHome.buildsection')),
            ],
            options={
                'unique_together': {('build_section', 'created_at')},
            },
        ),
    ]
