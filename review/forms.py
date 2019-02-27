from django import forms

from review.models import hindu,comment


class ReviewForm(forms.ModelForm):

    class Meta:
        model = hindu
        fields = '__all__'
        labels = { "Title":"Title of study",
                    "Place_of_study":"Place of study",
                    "Prin_invest":"Principal Investigator",
                    "Name":"Name",
                    "Desig":"Designation",
                    "NAme_of_research_fellow":"Name of research fellow",
                    "Invitation_paragraph":"Invitation Paragraph",
                    "Intro":"Introduction",
                    "Why_am_i":"Why am I being requested to participate in this study",
                    "Duration":"Duration of individual patient participation",
                    "How_many":"How many subjects will be participating in the study",
                    "IS_my_part":"Is my participation Compulsory?",
                    "Can_i_withdraw":"Can I withdraw from the study",
                    "What_will_be_done":"What will be done at the first visit?",
                    "What_are_my_responsibility":"What are my responsibilities",
                    "What_are_risk":"What are the foreseeable risk/discomforts/inconvience involved",
                    "Confidentiality":"What about the confidentiality of my dada?",
                    "Whom_contact":"Whom can I contact for more information?"
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = comment
        fields = ("body",)

