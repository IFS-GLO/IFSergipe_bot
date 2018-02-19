from django.db import models


class Bot(models.Model):
    running = False
    next_command = ''
    last_command = ''

    class Meta:
        managed = False


class Chat(models.Model):
    username = models.TextField(null=True, verbose_name='Usuário')
    first_name = models.TextField(null=True, verbose_name='Primeiro nome')
    last_name = models.TextField(null=True, verbose_name='Último nome')
    is_running = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Última utilização')

    def __str__(self):
        return str(self.id)


class ChatUpdate(models.Model):
    command = models.CharField(max_length=20, verbose_name='Comando usado')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')

    chat = models.ForeignKey(Chat)


class Context(models.Model):
    text = models.TextField()
    chat = models.ForeignKey(Chat)
    position = models.IntegerField()


class Command(models.Model):
    title = models.TextField(max_length=45, verbose_name='Título')
    trigger = models.TextField(max_length=25, verbose_name='Comando')
    message = models.TextField(verbose_name='Mensagem')
    arguments = models.TextField(blank=True, verbose_name='Argumentos')
    next_trigger = models.ForeignKey('self', blank=True, null=True, verbose_name='Próximo comando')
