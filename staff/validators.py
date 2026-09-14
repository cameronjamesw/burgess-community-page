from django.core.exceptions import ValidationError


def validate_file_size(value):
    limit = 5 * 1024 * 1024  # 5 MB

    if hasattr(value, 'size'):
        if value.size > limit:
            raise ValidationError(
                'Image file size must be no more than 5 MB.'
            )
