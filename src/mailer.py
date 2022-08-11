from decouple import config
from requests import post


class Mailer:
    @staticmethod
    def send_summary(summary: str) -> None:
        data = {
            "from": f"mailgun@{config('DOMAIN_NAME')}",
            "to": [config('RECEIVER_MAIL_ADDRESS')],
            "subject": "Superhero Fight Simulator Summary",
            "html": summary
        }
        post(
            url=f"https://api.mailgun.net/v3/{config('DOMAIN_NAME')}/messages",
            auth=("api", config('API_KEY')),
            data=data
        )
