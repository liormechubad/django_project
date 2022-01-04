PASSWORD_CONFIG = [
    {
        'NAME': 'django_password_validators.password_history.password_validation.UniquePasswordsValidator',
        'OPTIONS': {
            # How many recently entered passwords matter.
            # Passwords out of range are deleted.
            # Default: 0 - All passwords entered by the user. All password hashes are stored.
            'last_passwords': 3  # Only the last 3 passwords entered by the user
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 10,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME': 'blog.validators.UniqueSymbolsValidator'
    },
    {
        'NAME': 'blog.validators.LetterCaseValidator'
    }
]
