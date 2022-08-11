from decouple import config
from requests import post


class Mailer:
    @classmethod
    def send_summary(cls, summary: str) -> None:
        print("domain name", config('DOMAIN_NAME'))
        print("RECEIVER_MAIL_ADDRESS", config('RECEIVER_MAIL_ADDRESS'))
        print("config('API_KEY')", config('API_KEY'))
        data = {
            "from": f"mailgun@{config('DOMAIN_NAME')}",
            "to": [config('RECEIVER_MAIL_ADDRESS')],
            "subject": "Superhero Fight Simulator Summary",
            "html": summary
        }
        response = post(
            url=f"https://api.mailgun.net/v3/{config('DOMAIN_NAME')}/messages",
            auth=("api", config('API_KEY')),
            data=data
        )
        print(response.status_code)
        print(response.json())
