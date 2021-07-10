from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210708_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(blank=True, to='products.Tag', verbose_name='Теги'),
        ),
    ]