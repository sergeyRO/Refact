from Mailer import Mailer

if __name__ == '__main__':
    login = 'login@gmail.com'
    password = 'qwerty'
    mailer = Mailer(login, password)

    subject = 'Subject'
    recipients = ['vasya@email.com', 'petya@email.com']
    message = 'Message'

    mailer.send_mess(subject, recipients, message)

    header = None
    mailer.recieve_mess(header)
