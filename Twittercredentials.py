import tweepy

consumer_key = "k0ODjXaYwPxKE2hbrFCLniNVj";
#eg: consumer_key = "YisfFjiodKtojtUvW4MSEcPm";


consumer_secret = "I3ztUmM2rajZZzkvAuseFpJgm6BPJQzxkGfYSccCHqEDTEcydg";
#eg: consumer_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token = "805941210-NpWQRBGhyyMTDWC865Pv96qMsyRHpjC08qvfuUzH";
#eg: access_token = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";

access_token_secret = "uV0RPrD1apueYqPGu1cYYn2SLADmNOBDdiWf2AS7Jdf2r";
#eg: access_token_secret = "YisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPmYisfFjiodKtojtUvW4MSEcPm";


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



