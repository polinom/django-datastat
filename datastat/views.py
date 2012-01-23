from django.db.models import get_model, Count
from django.shortcuts import render
from django.db import models


class ObjWrapper(object):
    def __init__(self,app_label, model_name):
        self.Model = get_model(app_label, model_name)
        self.model_info = {}
        for field in self.Model._meta.fields:
        	self.model_info[field.name] = dict(verbose_name=field.verbose_name.title())

    def analyse(self):
        for field in self.Model._meta.fields:
            if isinstance(field, models.CharField):
        	    self.analyseCharField(field)

            if isinstance(field, models.IntegerField)\
                or isinstance(field,models.PositiveIntegerField):
                self.analyseIntegerField(field)

            if isinstance(field, models.ForeignKey):
                self.analyseForeignKey(field)

            if isinstance(field, models.DateTimeField)\
                or isinstance(field,models.DateField)\
                or isinstance(field,models.TimeField):
                self.analyseDateTimeField(field)

    def analyseCharField(self,field):
        print field.db_type()
        print field.db_column

    def analyseIntegerField(self,field):
        print field.db_type()
        print field.db_column
        if field.choices:
        	print 'hello'

    def analyseForeignKey(self,field):
        print field.db_type()
        print field.db_column

    def analyseDateTimeField(self,field):
        print field.db_type()
        print field.db_column

    def get_coises_count(self,field):
        all = self.Model.objects.all().values(field.name).annotate(count=Count("pk")).order_by('-count')




def modelstat(request, app_label, model_name):
    wrapper = ObjWrapper(app_label, model_name)
    results = wrapper.analyse()

    return render(request, 'datastat/show_chart.html', {'model_info':wrapper.model_info})


