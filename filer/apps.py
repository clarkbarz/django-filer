# -*- coding: utf-8 -*-

from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _

import mptt


class FilerConfig(AppConfig):
    name = 'filer'
    verbose_name = _("django filer")

    def ready(self):
        Folder = self.get_model('Folder')
        try:
            mptt.register(Folder)
        except mptt.AlreadyRegistered:
            pass
