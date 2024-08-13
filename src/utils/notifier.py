import smtplib
from email.mime.text import MIMEText

class Notifier:
    """
    Notifier отправляет уведомления по электронной почте.
    """

    def __init__(self, cfg):
        self.server_cfg = cfg

    def notify(self, mail, lst):
        msg = MIMEText(f"Спасибо за прохождение опроса.\nВаш ввод:\n{lst}")
        msg['Subject'] = 'Результаты опроса'
        msg['From'] = self.server_cfg['user']
        msg['To'] = mail

        # Используем SMTP_SSL для подключения к порту 465
        with smtplib.SMTP_SSL(self.server_cfg['host'], self.server_cfg['port']) as server:
            server.login(self.server_cfg['user'], self.server_cfg['pass'])
            server.sendmail(self.server_cfg['user'], mail, msg.as_string())

    def execute(self, mail, lst):
        self.notify(mail, lst)
