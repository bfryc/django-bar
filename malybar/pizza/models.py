# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Pizza(models.Model):
    LARGE = 'L'
    MEDIUM = 'M'
    SMALL = 'S'
    ROZMIARY = (
        (LARGE, 'duża'),
        (MEDIUM, 'średnia'),
        (SMALL, 'mała'),
    )
    nazwa = models.CharField(verbose_name='Pizza', max_length=30)
    opis = models.TextField(blank=True, help_text='Opis Pizzy')
    rozmiar = models.CharField(max_length=1, choices=ROZMIARY, default=LARGE)
    cena = models.DecimalField(max_digits=5, decimal_places=2)
    data = models.DateField('dodano', auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __unicode__(self):
        return u'%s' % (self.nazwa)

    class Meta:
        verbose_name_plural = 'pizze'


class Skladnik(models.Model):
    pizza = models.ForeignKey(Pizza, related_name='skladniki')
    nazwa = models.CharField(verbose_name=u"składnik", max_length=30)
    jarski = models.BooleanField(
        default=False,
        verbose_name=u"jarski?",
        help_text=u"Zaznacz, jeżeli składnik jest odpowiedni dla"
        u" wegetarian")

    def __unicode__(self):
        return u'%s' % (self.nazwa)

    class Meta:
        verbose_name_plural = u'Składniki'
