def validacion(mail):
    mail = mail.strip()
    if mail.startswith(("@",".")) or mail.endswith(("@",".")):
        return False
    elif mail.count("@")==1 and mail.endswith((".com", ".ar")):
        return True
    return False