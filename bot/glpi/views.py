from pprint import pprint

from glpi.models import *


def get_ticket(pk):
    try:
        instance = Tickets.objects.get(id=pk)
        follow_ups = TicketFollowUps.objects.filter(ticket=instance)
        instance.follows_ups = follow_ups

        pprint(instance)

        return {'msg': False, 'instance': instance}

    except Tickets.DoesNotExist:
        return {'msg': True, 'text': 'Chamado não encontrado'}


def add_ticket(instance):
    new_instance = Tickets(instance=instance).save()
    if new_instance.id:
        return {'msg': True, 'text': 'Cadastrado com sucesso!'}
