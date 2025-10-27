from django.db import migrations, models
import django.db.models.deletion


def populate_author_fk(apps, schema_editor):
    Book = apps.get_model("books", "Book")
    Author = apps.get_model("books", "Author")
    for book in Book.objects.all():
        # The existing 'author' is a CharField at this stage
        name = getattr(book, "author", None)
        if name:
            author_obj, _ = Author.objects.get_or_create(name=str(name))
            setattr(book, "author_tmp", author_obj)
            book.save(update_fields=["author_tmp"])


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="author_tmp",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="books.author",
            ),
        ),
        migrations.RunPython(
            populate_author_fk, reverse_code=migrations.RunPython.noop
        ),
        migrations.RemoveField(
            model_name="book",
            name="author",
        ),
        migrations.RenameField(
            model_name="book",
            old_name="author_tmp",
            new_name="author",
        ),
        migrations.AlterField(
            model_name="book",
            name="release_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
