from django.db import models

# Create your models here.


class Place(models.Model):

	# ip = models.GenericIPAddressField(protocol=both, unpack_ipv4=False)
	ip_address = models.CharField(max_length=40, default='ipX', blank=False,)
	ref_id = models.CharField(max_length=40, default='XXX', unique=True)

	iwent = models.CharField(max_length=120, default='', blank=True,)
	iam = models.CharField(max_length=120, default='Toulouse', blank=False,)
	igo = models.CharField(max_length=120, default='', blank=True,)

	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)

	def __unicode__(self):
		return self.iwent

	class Meta:
		unique_together = ("ref_id", "iwent", "iam", "igo")