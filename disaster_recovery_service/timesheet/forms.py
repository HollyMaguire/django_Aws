from django import forms
from django.forms import formset_factory
from .models import Timecard, Job_code_managment, Timecard_Job_code_managment
from django.utils import timezone

class HoursWorkedForm(forms.Form):
    job_code_managment = forms.ModelMultipleChoiceField(
        queryset=Job_code_managment.objects.all(),
        widget=forms.Select,
        # widget=forms.CheckboxSelectMultiple,
    )
    hours_worked = forms.DecimalField(label="Hours worked", min_value=0, decimal_places=2)

class CreateTimeCardForm(forms.ModelForm):
    job_code_managment = forms.ModelMultipleChoiceField(
        queryset=Job_code_managment.objects.all(),
        widget=forms.Select, # dont use select it wont work
        # widget=forms.CheckboxSelectMultiple,
    )
    hours_worked = forms.DecimalField(label="Hours worked", min_value=0, decimal_places=2)

    job_code_managment_1 = forms.ModelMultipleChoiceField(
        queryset=Job_code_managment.objects.all(),
        widget=forms.Select,
        # widget=forms.CheckboxSelectMultiple,
    )
    hours_worked_1 = forms.DecimalField(label="Hours worked", min_value=0, decimal_places=2)

    job_code_managment_2 = forms.ModelMultipleChoiceField(
        queryset=Job_code_managment.objects.all(),
        widget=forms.SelectMultiple,
        # widget=forms.CheckboxSelectMultiple,
    )
    hours_worked_2 = forms.DecimalField(label="Hours worked", min_value=0, decimal_places=2)

    # super_total = hours_worked + hours_worked_1 + hours_worked_2
    # HoursWorkedFormSet = formset_factory(HoursWorkedForm)
    # formset = HoursWorkedFormSet(initial=[
    #  {'job_code_managment': Job_code_managment.objects.first(),
    #   'hours_worked': 0,}
    #  ])
    #
    # for form in formset:
    #     formset

    class Meta:
        model = Timecard
        fields = ['site_code', 'contractor_name', 'date','job_code_managment']
        # fields = []

    def save(self, *args, **kwargs):
        # Check how the current values differ from ._loaded_values. For example,
        # prevent changing the creator_id of the model. (This example doesn't
        # support cases where 'creator_id' is deferred).
        super().save(*args, **kwargs)

        time_card = Timecard.objects.last()

        job_code_managments = [self.cleaned_data["job_code_managment"].first(),
                              self.cleaned_data["job_code_managment_1"].first(),
                              self.cleaned_data["job_code_managment_2"].first()]

        hours_worked_total = [self.cleaned_data["hours_worked"],
                              self.cleaned_data["hours_worked_1"],
                              self.cleaned_data["hours_worked_2"]]

        for job_code_managment in job_code_managments:
            job_code_managment_id = job_code_managment.id


            Timecard_Job_code_managment(
                hours_worked=hours_worked_total.pop(0),
                time_card=time_card,
                job_code_managment_id=job_code_managment_id
            ).save()


        # Timecard(site_code=self.site_code, contractor_name=self.contractor_name,
        #          date=self.date).save()
        print("hello")
