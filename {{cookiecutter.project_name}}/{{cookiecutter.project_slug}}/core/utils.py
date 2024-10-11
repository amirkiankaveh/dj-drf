def normalize_phone_number(phone_number):
    if not phone_number.startswith("+98"):
        if phone_number.startswith("0"):
            phone_number = phone_number[1:]
        elif phone_number.startswith("98"):
            phone_number = phone_number[2:]
        phone_number = "+98" + phone_number
    return phone_number
