from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
from .models import User


# @receiver(post_save, sender=SocialAccount)
# def set_social_user_type(sender, instance, created, **kwargs):
#     if created:
#         user = instance.user
#         # Default Google signups to homeowner
#         # They can change later in settings
#         if not user.user_type:
#             user.user_type = User.HOMEOWNER
#             user.save()