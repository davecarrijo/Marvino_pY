from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello","hie","sup","ola","oi"):
        return "Eae otario!!!"

    if user_message in ("quem é você?"):
        return "Eu sou um bot"

    if user_message in ("/serova"):
        return "para de ser negro, o CARIOCA"

    if user_message in ("tempo","time"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "Ainda não tem os comandos completos"
