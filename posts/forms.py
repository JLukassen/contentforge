from django import forms

from .models import SocialPost


class SocialPostForm(forms.ModelForm):
    class Meta:
        model = SocialPost
        fields = [
            "title",
            "master_text",
            "hashtags",
            "scheduled_for",
            "status",
        ]

        widgets = {
            "master_text": forms.Textarea(attrs={"rows": 8}),
            "hashtags": forms.TextInput(
                attrs={"placeholder": "kpop illit contentcreation"}
            ),
            "scheduled_for": forms.DateTimeInput(
                attrs={"type": "datetime-local"}
            ),
        }
