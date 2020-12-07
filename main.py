import datetime as dt
from utils.textProcessor import TextProcessor
from utils.twitterManager import TwitterManager

def tweet_headlines(scraper, url, element_scraper, attribute, element_parser, attribute_parser, n_headlines=3):
    # Scrape headlines and articles
    df = scraper.scrape_site(url=url, 
    	                     element=element_scraper, 
    	                     attribute=attribute)

    df_filtered = df[:n_headlines].copy()
    if 'reuters' in url:
        df_filtered['article'] = df_filtered['link'].apply(lambda x: scraper.parse_article(url=x, element=element_parser, attribute=attribute_parser))
    else:
        df_filtered['article'] = df_filtered['link'].apply(lambda x: scraper.parse_article(url=x, element=element_parser))

    # Process scraped articles
    tp = TextProcessor()
    df_filtered['cleaned_text'] = df_filtered['article'].apply(lambda x: tp.clean_text(x))
    df_filtered['cleaned_summary'] = df_filtered['summary'].apply(lambda x: tp.clean_text(x))
    df_filtered['token_frequencies'] = df_filtered.apply(lambda x: tp.get_word_token_frequencies(x['cleaned_text'], n_tokens=5), axis=1)
    df_filtered['url_short'] = df_filtered['link'].apply(lambda x: tp.shorten_url(x)['url'])

    print(df_filtered.head())
    print(df_filtered['token_frequencies'].head())

    # Post to twitter
    tm = TwitterManager()
    tm.authenticate()

    headline = df_filtered['headline']
    summary = df_filtered['summary']
    url_shortened = df_filtered['url_short']
    top_keywords = df_filtered['token_frequencies']
    source = url.split('www.', 1)[1].split('.co')[0]

    for i in range(n_headlines):
        message = f"[{dt.datetime.today().strftime('%Y-%m-%d %H:%M')}] {source.upper()} Top Headline ({str(i+1)} of {str(n_headlines)}): " + \
                  f"{headline[i]}. {summary[i]} {url_shortened[i]} #{' #'.join(top_keywords[i].keys())}"
        print(len(message))
        # try:
        # 	tm.post_tweet(message=message)
        # except Exception as e:
        #     print(e)
        #     continue
