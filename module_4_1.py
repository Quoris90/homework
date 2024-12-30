def send_email(message, recipient, *, sender="university.help@gmail.com"):
    # Проверка корректности email
    valid_domains = (".com", ".ru", ".net")
    if "@" not in recipient or not recipient.endswith(valid_domains) or "@" not in sender or not sender.endswith(
            valid_domains):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверка на отправку самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка отправителя
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
