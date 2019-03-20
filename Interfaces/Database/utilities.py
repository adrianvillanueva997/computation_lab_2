class Utilities:
    def __init__(self):
        pass

    def scrape_text_for_sql(self, text):
        text = str(text).replace('\'', '\'\'')
        text = text.replace('\"', '\"\"')
        text = text.replace('%', '%%')
        return text
