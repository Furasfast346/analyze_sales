from gigachat import GigaChat

giga = GigaChat(verify_ssl_certs=False,
                credentials='MDE5ZTExZjMtNjk4Zi03ZTNlLTlhOGYtZDBkNGE1ZDlmOWYyOmUzZTAwOTg1LTVjOGItNGJmZS05MjJhLWIzYTUwZDczZGI2Yw==',
                model='GigaChat-2')

def create_suggestions(data) -> str:
    response = giga.chat(
    "Я отправлю тебе JSON-отчет о продажах в ресторане, предложи свои варианты по оптимизации и увеличению выручки, ограничься короткой лаконичной рекомендацией. Не используй символов разметки вообще, отвечай одной строкой. Вот JSON: " + str(data))

    return response.choices[0].message.content
