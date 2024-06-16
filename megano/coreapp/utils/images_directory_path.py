
def banner_images_directory_path(instance, filename: str) -> str:
    return 'banners/banner_{pk}/{filename}'.format(pk=instance.pk, filename=filename)
