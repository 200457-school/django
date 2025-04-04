from django.db import models
from django.contrib.auth import get_user_model


class Schedule(models.Model):
    SCHEDULE_TYPE = (
        ("P", "Solar Panels"),
        ("C", "Electric Vehicle (EV) Charging Stations"),
        ("S", "Smart Home Energy Management Systems"),
    )
    ACTION = (
        ("I", "Installation"),
        ("C", "Consultation")
    )
    TIME_SLOT = (
        (0, "9:00 - 10:00"),
        (1, "10:00 - 11:00"),
        (2, "11:00 - 12:00"),
        (3, "12:00 - 13:00"),
        (4, "13:00 - 14:00"),
        (5, "14:00 - 15:00"),
        (6, "15:00 - 16:00"),
        (7, "16:00 - 17:00"),
    )
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    schedule_type = models.CharField(max_length=1, choices=SCHEDULE_TYPE)
    action = models.CharField(max_length=1, choices=ACTION)
    time_slot = models.IntegerField(choices=TIME_SLOT)
    date = models.DateField()

    class Meta:
        ordering = ["-date"]
        constraints = [
            models.UniqueConstraint(fields=["schedule_type", "action", "date", "time_slot"], name="unique_schedule")
        ]

    @property
    def time(self):
        return self.TIME_SLOT[self.time_slot][1]

    @property
    def action_name(self):
        return dict(self.ACTION).get(self.action, "Unknown")

    @property
    def schedule_type_name(self):
        return dict(self.SCHEDULE_TYPE).get(self.schedule_type, "Unknown")

    def __str__(self):
        return f"{self.schedule_type_name} - {self.action_name} - {self.date} - {self.time}"
