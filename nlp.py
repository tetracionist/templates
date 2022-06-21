class nlp(object):
  def __init__(self, df, text_column, ngram_words=2, num_topics=5):
    self.df = df
    self.text_column = text_column
    self.ngram_words = ngram_words
    self.num_topics = num_topics
    self.df = self.df.toPandas() # Only required if you have a pyspark dataframe
    
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
    df = pd.DataFrame(columns=['topic_'+str(i+1) for i in range(self.num_topics)])
    for topic_idx, topic in enumerate(svd_components):
      top_features_ind = topic.argsort()[:-self.num_topics - 1:-1]
      top_features = [feature_names[i] for i in top_features_ind]
      df_length = len(df)
      df.loc[df_length] = top_features
    return df
    
