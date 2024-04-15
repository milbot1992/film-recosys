def get_image_url(new_poster_path, size='w500'):
    base_url = "https://image.tmdb.org/t/p/"
    new_image_url = f"{base_url}{size}{new_poster_path}"
    return new_image_url