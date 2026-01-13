from django.core.exceptions import ValidationError

"""
    Creons nos propres validateurs de mdp.
    Un validateur est une class qui n'as besoins que de
    deux methodes:
        - validate
        - get_help_text
"""


class ContainsLetterValidator:
    def validate(self, password, user=None):
        if not any(char.isalpha() for char in password):
            raise ValidationError(
                "Le mot de passe n'est pas valide", code="password_no_letters"
            )

    def get_help_text(self):
        return (
            "Le mot de passe doit contenir au moins une lettre majuscule ou minuscule"
        )
