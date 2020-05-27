
class SpacyMixin():
    nlp = None 

    def _load_nlp(self):
        if SpacyMixin.nlp == None:
            import es_core_news_md
            print("NLP is not yet loaded")
            SpacyMixin.nlp = es_core_news_md.load()
            print("NLP loaded")
