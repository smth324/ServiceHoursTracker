from django.db import models
from django.contrib.auth.models import User
from django import forms


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=6, unique=True)

    required_service_hours = models.FloatField(default=20.0)
    completed_service_hours = models.FloatField(default=0.0)
    penalty_service_hours = models.FloatField(default=0.0)
    
    def remaining_service_hours(self):
        return max(0.0, (self.required_service_hours + self.penalty_service_hours) - self.completed_service_hours)

class OrgProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)


class OAAProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=50)
    service_hours = models.IntegerField()
    number_of_students = models.IntegerField()
    role_descriptions = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    organizer = models.ForeignKey(
        OrgProfile, on_delete=models.CASCADE, related_name="events"
    )
    approved = models.BooleanField(default=False)
    students = models.ManyToManyField(
        StudentProfile, through="Participation", related_name="events"
    )

    def remaining_slots(self):
        assigned_count = self.participation_set.count()
        return max(0, self.number_of_students - assigned_count)

    def is_user_in_event(self, user):
        try:
            student_profile = user.studentprofile
        except StudentProfile.DoesNotExist:
            return False

        return Participation.objects.filter(
            student=student_profile, event=self
        ).exists()
    
    def is_full(self):
        return self.participation_set.count() >= self.number_of_students


class Participation(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ("student", "event")


class ClassSchedule(models.Model):
    student = models.ForeignKey(
        "StudentProfile", on_delete=models.CASCADE, related_name="class_schedules"
    )
    day_of_week = models.CharField(
        max_length=10,
        choices=[
            ("Monday", "Monday"),
            ("Tuesday", "Tuesday"),
            ("Wednesday", "Wednesday"),
            ("Thursday", "Thursday"),
            ("Friday", "Friday"),
            ("Saturday", "Saturday"),
            ("Sunday", "Sunday"),
        ],
    )
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.subject} - {self.day_of_week} {self.start_time}-{self.end_time}"


class ClassScheduleForm(forms.ModelForm):
    class Meta:
        model = ClassSchedule
        fields = ["day_of_week", "start_time", "end_time", "subject"]
