from django.db import migrations


def create_reference_pages(apps, schema_editor):
    Site = apps.get_model("sites", "Site")
    FlatPage = apps.get_model("flatpages", "FlatPage")

    site, _ = Site.objects.update_or_create(
        pk=1,
        defaults={"domain": "localhost:8000", "name": "SkillFactory Django Demo"},
    )

    pages = [
        {
            "url": "/about/",
            "title": "О проекте",
            "content": (
                "Это первая статическая страница Django FlatPages. "
                "Она использует общий Bootstrap-шаблон и пользовательский контент."
            ),
            "template_name": "flatpages/about.html",
            "registration_required": False,
        },
        {
            "url": "/styled/",
            "title": "Страница со стилями",
            "content": (
                "Этот пользовательский текст намеренно выводится два раза без изменения "
                "переменной flatpage.content."
            ),
            "template_name": "flatpages/styled.html",
            "registration_required": False,
        },
        {
            "url": "/private/",
            "title": "Закрытая страница",
            "content": (
                "Эта статическая страница доступна только вошедшему пользователю "
                "с правами staff/admin."
            ),
            "template_name": "flatpages/private.html",
            "registration_required": True,
        },
    ]

    for data in pages:
        page, _ = FlatPage.objects.update_or_create(
            url=data["url"],
            defaults={
                "title": data["title"],
                "content": data["content"],
                "template_name": data["template_name"],
                "registration_required": data["registration_required"],
            },
        )
        page.sites.set([site])


def remove_reference_pages(apps, schema_editor):
    FlatPage = apps.get_model("flatpages", "FlatPage")
    FlatPage.objects.filter(url__in=["/about/", "/styled/", "/private/"]).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        ("flatpages", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_reference_pages, remove_reference_pages),
    ]
