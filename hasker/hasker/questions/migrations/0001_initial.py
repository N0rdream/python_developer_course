# Generated by Django 2.1 on 2018-09-28 21:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import questions.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='answers', to=settings.AUTH_USER_MODEL)),
                ('d_voters', models.ManyToManyField(blank=True, related_name='answer_downvoters', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(questions.models.VoteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('date_pub', models.DateTimeField(auto_now_add=True)),
                ('is_hidden', models.BooleanField(default=False)),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to=settings.AUTH_USER_MODEL)),
                ('best_answer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parent_question', to='questions.Answer')),
                ('d_voters', models.ManyToManyField(blank=True, related_name='question_downvoters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_pub'],
            },
            bases=(questions.models.VoteMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.ManyToManyField(related_name='questions', to='questions.Tag'),
        ),
        migrations.AddField(
            model_name='question',
            name='u_voters',
            field=models.ManyToManyField(blank=True, related_name='question_upvoters', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='answers', to='questions.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='u_voters',
            field=models.ManyToManyField(blank=True, related_name='answer_upvoters', to=settings.AUTH_USER_MODEL),
        ),
    ]
