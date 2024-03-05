
from django.db import models

## dynbamic POC 

class Mtable(models.Model):
    name = models.CharField(max_length=255)
    class Meta:  
        db_table = "mtable" 

class Mfield(models.Model):
    table = models.ForeignKey(Mtable, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=32)
    class Meta:  
        db_table = "mfield" 

class MRelationship(models.Model):
    metadata_table = models.ForeignKey(Mtable, related_name='metadata_table_relationships', on_delete=models.CASCADE)
    related_table = models.ForeignKey(Mtable, related_name='related_table_relationships', on_delete=models.CASCADE)
    related_field = models.ForeignKey(Mfield, on_delete=models.CASCADE)
    class Meta:  
        db_table = "mrelationship" 

field_types = {
    'AutoField': models.AutoField(),
    'BigIntegerField': models.BigIntegerField(),
    'BooleanField': models.BooleanField(),
    'CharField': models.CharField(max_length=255),
    'DateField': models.DateField(),
    'DateTimeField': models.DateTimeField(),
    'DecimalField': models.DecimalField(max_digits=10, decimal_places=2),
    'DurationField': models.DurationField(),
    'EmailField': models.EmailField(max_length=254),
    'FileField': models.FileField(upload_to=''),
    'FloatField': models.FloatField(),
    'ForeignKey': models.ForeignKey('self', on_delete=models.CASCADE),
    'ImageField': models.ImageField(upload_to=''),
    'IntegerField': models.IntegerField(),  
    'ManyToManyField': models.ManyToManyField('self'),
    'NullBooleanField': models.NullBooleanField(),
    'PositiveIntegerField': models.PositiveIntegerField(),
    'PositiveSmallIntegerField': models.PositiveSmallIntegerField(),
    'SlugField': models.SlugField(max_length=255),
    'SmallIntegerField': models.SmallIntegerField(),
    'TextField': models.TextField(),
    'TimeField': models.TimeField(),
    'URLField': models.URLField(max_length=200),
    'UUIDField': models.UUIDField(),
}
