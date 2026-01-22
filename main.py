test_settings = {
    "theme": "dark",
    "language": "en",
    "notifications": True
}


def add_setting(settings, key_value_pair):
    key, value = key_value_pair

    key = str(key).lower()
    value = str(value).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"
