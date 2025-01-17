# Generated by Django 3.2.13 on 2022-07-05 12:23

from django.db import migrations, models
from django.db.backends.postgresql.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps


def fix_wildcard_mention_policy_stream_admins_value(
    apps: StateApps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    Realm = apps.get_model("zerver", "Realm")
    WILDCARD_MENTION_POLICY_STREAM_ADMINS = 4
    WILDCARD_MENTION_POLICY_ADMINS = 5
    Realm.objects.filter(wildcard_mention_policy=WILDCARD_MENTION_POLICY_STREAM_ADMINS).update(
        wildcard_mention_policy=WILDCARD_MENTION_POLICY_ADMINS
    )


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0394_alter_realm_want_advertise_in_communities_directory"),
    ]

    operations = [
        migrations.AlterField(
            model_name="realm",
            name="wildcard_mention_policy",
            field=models.PositiveSmallIntegerField(default=5),
        ),
        migrations.RunPython(fix_wildcard_mention_policy_stream_admins_value, elidable=True),
    ]
