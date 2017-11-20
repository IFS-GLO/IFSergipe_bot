from django.db import models


class Bot(models.Model):
    running = False
    next_command = ''
    last_command = ''
