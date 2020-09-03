# Text Sentiment Prediction API
Simple API for text sentiment analysis using Machine Learning and Natural Language Processing

The Live API is available on https://textsentimentapi.herokuapp.com/

You can use it by making a GET request with JSON Object with parameter "query" and review text as value


# Example Uses

## Example 1
`https://textsentimentapi.herokuapp.com/predictsentiment?query="Three Idiots is a remarkable ahead of its time Bollywood blockbuster. This film is a comedy movie with strong acting, memorable characters, a perplexing storyline and most importantly, highly motivational movie to choose the right path in your life"`

### Result:
`{"prediction": "Positive", "confidence": 0.92}`


## Example 2
`https://textsentimentapi.herokuapp.com/predictsentiment?query="On the whole Race 3 is not entirely unentertaining but it is majorly disappointing"`
### Result: 
`{"prediction": "Negative", "confidence": 0.285}`
