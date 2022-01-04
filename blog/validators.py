from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _
import string
import re


class UniqueSymbolsValidator:
    def __init__(self, special_symbols=('~', '!', '@', '#', '$', '%', '^', '&', '*')):
        self.special_symbols = special_symbols

    def validate(self, password, user=None):
        have_special_symbol = False
        for symbol in self.special_symbols:
            if symbol in password:
                have_special_symbol = True
        if not have_special_symbol:
            raise ValidationError(
                message="This password must contain at least one special symbol(~,!,@,#,$,%,^,&,*)")

    def get_help_text(self):
        return _(
            "Your password must contain at least one special symbol(~,!,@,#,$,%,^,&,*)"
        )


class LetterCaseValidator:
    def __init__(self, upper_case_letters=tuple(string.ascii_uppercase[:26]), lower_case_letters=tuple(string.ascii_lowercase[:26]), numbers=range(0, 10)):
        self.upper_case_letters = upper_case_letters
        self.lower_case_letters = lower_case_letters
        self.numbers = numbers

    def validate(self, password, user=None):
        lower_case_letter_exist = False
        for lower_case_letter in self.lower_case_letters:
            if lower_case_letter in password:
                lower_case_letter_exist = True
                break
        upper_case_letter_exist = False
        for upper_case_letter in self.upper_case_letters:
            if upper_case_letter in password:
                upper_case_letter_exist = True
                break
        number_exist = False
        for number in self.numbers:
            if str(number) in password:
                number_exist = True
                break
        if not lower_case_letter_exist:
            raise ValidationError(
                message="Password must contain at least one lowercase letter")
        if not upper_case_letter_exist:
            raise ValidationError(
                message="Password must contain at least one uppercase letter")
        if not number_exist:
            raise ValidationError(
                message="Password must contain at least one number")

    def get_help_text(self):
        return _(
            "Your password must contain at least one uppercase letter and one lower case letter and one number"
        )
