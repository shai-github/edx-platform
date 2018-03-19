"""
Django Signal related functionality for user_api accounts
"""

from django.dispatch import Signal

UserRetireMailingsSignal = Signal(providing_args=["user"])
