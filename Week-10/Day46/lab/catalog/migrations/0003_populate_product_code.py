from django.db import migrations


def populate_product_code(apps, schema_editor):
    Product = apps.get_model("catalog", "Product")

    for product in Product.objects.all():
        product.code = str(product.pk)
        product.save(update_fields=["code"])


def clear_product_code(apps, schema_editor):
    Product = apps.get_model("catalog", "Product")

    Product.objects.update(code=None)


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0002_add_product_code"),
    ]

    operations = [
        migrations.RunPython(
            populate_product_code,
            clear_product_code,
        ),
    ]
