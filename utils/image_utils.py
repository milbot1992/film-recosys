import logging

def get_image_url(new_poster_path, size='w500'):
    """
    Generate a URL for an image poster based on its path and size.

    Args:
        new_poster_path (str): The poster's path.
        size (str): The size of the poster. Defaults to 'w500'.

    Returns:
        str: The URL of the image.
    """
    base_url = "https://image.tmdb.org/t/p/"
    new_image_url = f"{base_url}{size}{new_poster_path}"

    logging.info("Generated image URL: %s", new_image_url)

    return new_image_url
