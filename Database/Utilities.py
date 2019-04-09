class Utilities:
    def __init__(self):
        pass

    @staticmethod
    def scrape_text_for_sql(text):
        text = str(text).replace('\'', '\'\'')
        text = text.replace('\"', '\"\"')
        text = text.replace('%', '%%')
        return text
