import datetime


LAST_UPGRADE = {}

def check_time():

    """
    Проверяет необходимость обновления товара на главной странице в разделе Ограниченный ассортимент
    True - если требуется обновление
    """
    today = datetime.datetime.now()
    only_date = today.date
    if LAST_UPGRADE.get("last_upgrade") is not None:
        delta = LAST_UPGRADE.get("last_upgrade") - only_date
        if delta.days > 0:
            LAST_UPGRADE["last_upgrade"] = only_date
            return True

        else:
            return False

    else:

        LAST_UPGRADE["last_upgrade"] = only_date
        return True

