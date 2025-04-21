## COMP SCI 7417 - Assignment 2 - ANLP

This is the second assignment of Applied Natural Language Processing course at the University of Adelaide

### Python Libraries Prerequisites:

```
python==3.9.21
ast
bs4
collections
datetime
gensim==4.0.1
json
matplotlib==3.9.0
nltk==3.9.1
os
pandas==2.2.3
requests==2.32.3
sentence-transformers==4.0.2
scikit-learn==1.6.1
spacy==3.8.3
string 
time
wordcloud==1.9.4
```

### How to Get Stack Exchange Access Token

#### Prerequisites:
1. Created Account on StackExchange. To create account, visit this page: [Stack Exchange Account](https://stackapps.com/users/login?returnurl=/app/oauth)

2. Installed Flask on local computer. Install via this command

```
pip install flask
```

##### Steps:

1. Open [this link](https://stackapps.com/apps/oauth/register) and  fill in this form and click submit:

``` 
- OAuth Domain (without http protocol): localhost 
- Application Website: http://localhost
- Checked "Enable Client Side OAuth Flow"
- The rest form can be anything
```

2. After that, you will get Client ID, Client Secret, and Key, save their values.

3. Open app.py file, and set this variables:

```
- CLIENT_SECRET -> Client Secret from StackExchange
- CLIENT_ID -> Client ID from StackExchange
```

4. Open Terminal, and run `python app.py`

5. Open Browser and access localhost, you will be asked to approve OAuth using your StackExchange Account

6. Once you approve, you will get the Access Token

7. Use the Access Token and Key from Stack Exchange to the jupyter notebooks,specifically set them to these two variables `ACCESS_TOKEN` and `API_KEY` respectively
