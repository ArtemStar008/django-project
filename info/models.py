from django.db import models


class InfoBlog(models.Model):
    """

    """

    text = models.TextField()
    name = models.CharField(max_length=30, null=False)
    rating = models.PositiveSmallIntegerField(null=False)
    price = models.FloatField(null=False)
    is_deleted = models.BooleanField(null=False, default=False)
    date = models.DateField(verbose_name='DateField')
    datetime = models.DateTimeField()



