import threading

from kafka.streaming_job import streaming

subreddits = ['india', 'usa', 'unitedkingdom', 'australia', 'russia', 'China', 'unitedkingdom', 'japan', 'france',
              'germany', 'italy', 'brazil', 'canada']
threads = []

for subreddit in subreddits:
    thread = threading.Thread(
        target=streaming,
        args=(subreddit,)
    )
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
