from django.db import models
from django.utils.translation import gettext_lazy as _
from facility.models import Facility
from config.settings import AUTH_USER_MODEL


class Rating(models.Model):
    class Range(models.IntegerChoices):
        RATING_1 = 1, _("Poor")
        RATING_2 = 2, _("Fair")
        RATING_3 = 3, _("Good")
        RATING_4 = 4, _("Very Good")
        RATING_5 = 5, _("Excellent")

    rater = models.ForeignKey(
        AUTH_USER_MODEL,
        verbose_name=_("User providing the rating"),
        on_delete=models.SET_NULL,
        null=True,
    )
    facility = models.ForeignKey(
        Facility,
        verbose_name=_("Facility being rated"),
        related_name="service_review",
        on_delete=models.SET_NULL,
        null=True,
    )
    rating = models.IntegerField(
        verbose_name=_("Rating"),
        choices=Range.choices,
        help_text="1=Poor, 2=Fair, 3=Good, 4=Very Good, 5=Excellent",
        default=0,
    )
    comment = models.TextField(verbose_name=_("Comment"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["rater", "facility"]

    def __str__(self):
        return f"{self.facility} rated at {self.rating}"
