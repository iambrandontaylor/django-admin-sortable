# Generated by Django 2.0 on 2017-12-05 02:55

import adminsortable.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BackwardCompatibleWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Backward Compatible Widget',
                'verbose_name_plural': 'Backward Compatible Widgets',
                'ordering': ['order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('order', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('order', models.PositiveIntegerField(default=0, editable=False)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Given name', max_length=30)),
                ('last_name', models.CharField(help_text='Family name', max_length=30)),
                ('order', models.PositiveIntegerField(default=0, editable=False)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='CustomWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('custom_order_field', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
            ],
            options={
                'verbose_name': 'Custom Widget',
                'verbose_name_plural': 'Custom Widgets',
                'ordering': ['custom_order_field'],
            },
        ),
        migrations.CreateModel(
            name='CustomWidgetComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('widget_order', models.PositiveIntegerField(db_index=True, default=0, editable=False)),
                ('custom_widget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.CustomWidget')),
            ],
            options={
                'verbose_name': 'Custom Widget Component',
                'verbose_name_plural': 'Custom Widget Components',
                'ordering': ['widget_order'],
            },
        ),
        migrations.CreateModel(
            name='GenericNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('object_id', models.PositiveIntegerField(verbose_name='Content id')),
                ('order', models.PositiveIntegerField(default=0, editable=False)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generic_notes', to='contenttypes.ContentType', verbose_name='Content type')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='NonSortableCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Non-Sortable Category',
                'verbose_name_plural': 'Non-Sortable Categories',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NonSortableCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Given name', max_length=30)),
                ('last_name', models.CharField(help_text='Family name', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='NonSortableNote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
                ('order', models.PositiveIntegerField(default=0, editable=False)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('is_board_member', models.BooleanField(default=False, verbose_name='Board Member')),
                ('order', models.PositiveIntegerField(default=0, editable=False)),
            ],
            options={
                'verbose_name_plural': 'People',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('order', models.PositiveIntegerField(default=0, editable=False)),
                ('category', adminsortable.fields.SortableForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.Category')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='SortableCategoryWidget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('order', models.PositiveIntegerField(default=0, editable=False)),
                ('non_sortable_category', adminsortable.fields.SortableForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.NonSortableCategory')),
            ],
            options={
                'verbose_name': 'Sortable Category Widget',
                'verbose_name_plural': 'Sortable Category Widgets',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='SortableNonInlineCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('order', models.PositiveIntegerField(default=0, editable=False)),
                ('non_sortable_category', adminsortable.fields.SortableForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.NonSortableCategory')),
            ],
            options={
                'verbose_name': 'Sortable Non-Inline Category',
                'verbose_name_plural': 'Sortable Non-Inline Categories',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('order', models.PositiveIntegerField(default=0, editable=False)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.AddField(
            model_name='note',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.Project'),
        ),
        migrations.AddField(
            model_name='nonsortablenote',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.Project'),
        ),
        migrations.AddField(
            model_name='nonsortablecredit',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.Project'),
        ),
        migrations.AddField(
            model_name='credit',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.Project'),
        ),
        migrations.AddField(
            model_name='component',
            name='widget',
            field=adminsortable.fields.SortableForeignKey(on_delete=django.db.models.deletion.CASCADE, to='samples.Widget'),
        ),
    ]
