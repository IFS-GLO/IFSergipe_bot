from .models import *


class TicketRouter(Tickets):
    def db_for_read(self, model, **hints):
        return 'glpi'

    def db_for_write(self, model, **hints):
        return 'glpi'

    def allow_relation(self, model, **hints):
        return 'glpi'
