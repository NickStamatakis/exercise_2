Twitter application
*********************************
This application reads tweets from the Twitter streaming API, parses them, counts the number of each word in the stream of tweets, and writes the final results to a Postgres database.

To run this application, move this directory as the root user to an Amazon Web Instance connected to volume with a functioning Postgres. As the Postgres user, create a database called tcount and a table called tweetwordcount with a word column (nvarchar) and a count column (integer). Validate the Poastgres password is "pass".

The amazon instance should also be running on Python 2.7 and Storm version 0.9.3.2.2.4.2-2.

To capture the live data and setup/process the stream to the database, navigate to the directory tweetword count and enter the following command:
sparse run 

See the screenshot folder to view how the code will look. As long as this is running, the postgres database will continue to be updated.

There are two primary scripts to investigate the postgres database: finalresults.py and hisogram.py.

finalresults.py <word (opt)>- displays count for the number of times a specific word has appeared through the Twitter API. If no word is entered, this script generates a list of every word, along with the count.

histogram.py <n> <m> - displays words that have appeared between n and m times throught the Twitter API. N must be less than M.

