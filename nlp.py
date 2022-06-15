class nlp(object):
  def __init__(self, df, text_column, ngram_words=2, num_topics=5):
    self.df = df
    self.text_column = text_column
    self.ngram_words = ngram_words
    self.num_topics = num_topics
    self.df = self.df.toPandas()
    
  def clean_text(self, text):
    return re.sub('[^A-Z a-z]+', '', text).lower()
  
  def ngram(self, text):
    words = self.clean_text(text).split()
    ngrams = zip(*[words[i:] for i in range(self.ngram_words)])
    return ' '.join(["_".join(ngram) for ngram in ngrams])
  
  def vectorise(self, text):
    vectorizer = TfidfVectorizer()
    return vectorizer.fit(text)
    #vectorizer.vocabulary_

    #data_vectorised = vectorizer.transform(text)
    #vectorised_words = vectorizer.get_feature_names()
    #feature_names = vectorizer.get_feature_names()
  
  def decompose(self, data_vectorised):
    svd = TruncatedSVD(n_components=5, random_state=42)
    return svd.fit(data_vectorised) 
    
  def topic_model(self, svd_components):
    for topic_idx, topic in enumerate(svd_components):
      print ("Topic %d:" % (topic_idx))
      components = [svd_components[0,i] for i in topic.argsort()[:-self.num_topics - 1:-1]]
      words = [feature_names[i] for i in topic.argsort()[:-self.num_topics - 1:-1]]
      print(components)
      print(words)
