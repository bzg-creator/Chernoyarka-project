from django.contrib.auth.models import Group, Permission, User
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from zones_app.models import Zone
from bookings_app.models import Booking


@receiver(post_migrate)
def setup_groups_and_admins(sender, **kwargs):
    managers_group, created = Group.objects.get_or_create(name='Managers')

    zone_content_type = ContentType.objects.get_for_model(Zone)
    booking_content_type = ContentType.objects.get_for_model(Booking)

    permissions = Permission.objects.filter(
        content_type__in=[zone_content_type, booking_content_type]
    )

    managers_group.permissions.set(permissions)

    if not User.objects.filter(username='manager').exists():
        manager_user = User.objects.create_user(
            username='manager',
            password='managerpassword',
            is_staff=True,
            is_superuser=False
        )
        manager_user.groups.add(managers_group)
        print("✅ Менеджер создан и добавлен в группу Managers")
    else:
        print("ℹ️ Менеджер уже существует")
