from requests import post


class Mailer:
    domain_name = "sandbox8604127af39f47ad80bed8a6113be467.mailgun.org"
    api_key = "2b7e824880e0b14192e1d5c39ac03fee-2bab6b06-ce4a1a80"
    treceiver_mail_address = "superheroapitestmail34@yopmail.com"

    @classmethod
    def send_summary(cls, summary: str) -> None:
        data = {
            "from": f"mailgun@{cls.domain_name}",
            "to": [cls.receiver_mail_address],
            "subject": "Superhero Fight Simulator Summary",
            "html": summary
        }
        post(
            url=f"https://api.mailgun.net/v3/{cls.domain_name}/messages",
            auth=("api", cls.api_key),
            data=data
        )
