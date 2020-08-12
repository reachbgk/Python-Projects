# from newsapi import NewsApiClient
from newsapi.newsapi_client import NewsApiClient
from datetime import datetime, timedelta

newsapi = NewsApiClient(api_key='7bd4a6636e864a38ba6a429f6aa1a166')

########################
#       headlines      #
########################
# /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='covid',
#                                           sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')


# top_headlines = newsapi.get_top_headlines(
#     q='World War',
#     language='en',
# )


########################
#    all artciles      #
########################
# /v2/everything
# all_articles = newsapi.get_everything(q='covid',
#                                       sources='cnn',
#                                       domains='cnn.com',
#                                       from_param='2020-04-01',
#                                       to='2017-12-12',
#                                       language='en',
#                                       sort_by='publishedAt',
#                                       page=2
#                                      )


# all_articles = newsapi.get_everything(
#     q='World War',
#     language='en',   
# )
# for article in top_headlines['articles']:
#     print('Title : ',article['title'])
#     print('Description : ',article['description'],'\n\n')


########################
#        sources       #
########################
# /v2/sources
# sources = newsapi.get_sources()

# news_sources = newsapi.get_sources()
# for source in news_sources['sources']:
#     print(source['name'])



##############################################################################
#   get all artciles for topics in keyword_list published in past 2 days     #
##############################################################################

d = datetime.today().date() - timedelta(days=2)
keyword_list = ['CDC', 'India']

f = open('result.txt', 'w')

for item in keyword_list:
    all_articles = newsapi.get_everything(
        q=item,
        from_param=d,
#         from_param='2020-04-01',
        sort_by='publishedAt',
        language='en')
    
    f.write("%s" % 'News for :' + item + '\n')
    f.write("%s" % 'Total Articles : ' + str(all_articles['totalResults']) + '\n\n')
    
#     print('News for :', item)
#     print('Total Articles : ', str(all_articles['totalResults']) + '\n')
    
    for article in all_articles['articles']:
#         print('Source : ',article['source']['name'])
#         print('Title : ',article['title'])
#         print('Description : ',article['description'],'\n\n')
        str1 = 'Source : ' + article['source']['name']
        str2 = 'Title : ' + article['title']
        str3 = 'Description : ' + article['description'] + '\n\n'

        f.write("%s\n" % str1)
        f.write("%s\n" % str2)
        f.write("%s\n" % str3)
        
f.close()



