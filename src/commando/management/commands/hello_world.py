import helpers

from typing import Any
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    
    def handle(self, *args: Any, **options: Any ) -> str | None:
        print("Hello World")