from django.db import models


class Tickets(models.Model):
    name = models.CharField(max_length=255, null=True)
    content = models.TextField()
    date = models.DateTimeField(null=True)
    close_date = models.DateTimeField(null=True, db_column='closedate')
    solve_date = models.DateTimeField(null=True, db_column='solvedate')

    class Meta:
        managed = False  # ignore migrate
        verbose_name = 'Chamado'

    def __str__(self):
        return self.name


class TicketFollowUps(models.Model):
    date = models.DateTimeField(null=True)
    content = models.TextField(null=True)
    date_creation = models.DateTimeField(null=True)
    date_mod = models.DateTimeField(null=True)
    position = models.IntegerField(db_column='timeline_position')

    ticket = models.ForeignKey(Tickets)

    class Meta:
        managed = False
        verbose_name = 'Acompanhamento'

    def __str__(self):
        return self.content


class Documents(models.Model):
    name = models.CharField(max_length=255, null=True)
    filename = models.CharField(max_length=255)
    comment = models.TextField(null=True)
    date_creation = models.DateTimeField(null=True)
    date_mod = models.DateTimeField(null=True)

    class Meta:
        managed = False
        verbose_name = 'Documento'

    def __str__(self):
        return self.name
