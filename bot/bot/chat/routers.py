from .models import *


class ChatRouter(Chat):
    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, model, **hints):
        return 'default'

    class Meta:
        managed = False


class ChatUpdateRouter(ChatUpdate):
    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, model, **hints):
        return 'default'

    class Meta:
        managed = False


class ChatContextRouter(Context):
    def db_for_read(self, model, **hints):
        return 'default'

    def db_for_write(self, model, **hints):
        return 'default'

    def allow_relation(self, model, **hints):
        return 'default'

    class Meta:
        managed = False
