from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import UserManager
import datetime




class Doctor(models.Model):

    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    gender = models.CharField(max_length=10, default='female')
    specialization = models.CharField('Specialization', max_length=50)
    info = models.TextField('Information', max_length=1250, blank=True)
    address = models.CharField(max_length=15 , null=True, blank=True)
    npi_number = models.CharField(max_length=12 , null=True, blank=False)
    state_license_number = models.CharField(max_length=12, null=True, blank=False)
    #profile_Pic = models.ImageField(upload_to=path_and_rename,verbose_name="Profile Picture", blank=True)
    #award_Pic = models.ImageField(upload_to=path_and_rename,verbose_name="Award_ Picture", blank=True)
    #consultation_fees = models.ImageField(upload_to=path_and_rename, verbose_name="Consultation Fees", blank=True)
    bio = models.IntegerField(default='0000$')

    def __str__(self):
        return self.title


class Customer(models.Model):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20,blank=True)
    gender = models.CharField(max_length=10,  default='female')


    #objects = CustomerManager()

    def __str__(self):
        return self.title


class Appointment(models.Model):
    start_time = models.TimeField('Start time')
    end_time = models.TimeField('End time')
    date = models.DateField('Date')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

#    class Meta:
#        ordering = ['start_time']

#    def __str__(self):
#        return str(self.start_time)

#    def get_absolute_url(self):
#        return f'/{self.doctor.id}/appoint/{self.id}'
#
#    def has_not_customer(self):         # TODO: change method to opposite(has_customer instead has_not_customer)
#        """
#            True if this appointment has not customer.
#            False if appointment already has customer.

#            :return: Boolean
#        """        return self.customer is None
    def is_outdated(self):
        """
        True if this appointment is outdated.
        False if appointment is still fresh.

        :return: Boolean
        """
        today = datetime.datetime.today()
        day = datetime.datetime.combine(self.date, self.start_time)
        return day <= today

    def is_working_day_appointment(self):
        """""
           True if this appointment is in working day.
           False if appointment is in weekend.

           :return: Boolean
        """""
        #function helps hide appointments on weekend
        return 0 <= self.date.weekday() <= 4

        has_not_customer.boolean = True
        has_not_customer.short_description = 'Has not customer?'

        is_outdated.boolean = True
        is_outdated.short_description = 'Is Outdated?'

        is_working_day_appointment.boolean = True
        is_working_day_appointment.short_description = 'Is in working day?'