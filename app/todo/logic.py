def check_description_length(description):
    if len(description) > 30:
        raise ValueError("Description should be within 30 characters.")
    if len(description) == 0:
        raise ValueError("Description should not be empty.")
    return True
