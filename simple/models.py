from django.db import models


class A(models.Model):
    a_name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.a_name


class B(models.Model):
    a_o2o = models.OneToOneField(A, primary_key=True)
    b_name = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s (%s)' % (self.b_name, self.a_o2o)