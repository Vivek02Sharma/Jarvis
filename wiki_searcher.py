import wikipedia

class WikiSearcher:
    def search_wikipedia(self, query):
        try:
            summary = wikipedia.summary(query, sentences=2)
            return f"According to Wikipedia:\n{summary}"
        except:
            return "Sorry, I couldn't find any information on that."
