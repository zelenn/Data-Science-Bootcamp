import logging

NUM_OF_STEPS = 3

REPORT_TEMPLATE = """Report

We have made {total} observations from tossing a coin: {tail_count} of them were tails and {head_count} of them were heads. The probabilities are {tail_frac:.2f}% and {head_frac:.2f}%, respectively. Our forecast is that in the next {num_steps} observations we will have: {forecast_tail} tail(s) and {forecast_head} head(s).
"""

TELEGRAM_WEBHOOK_URL = "https://api.telegram.org/bot800//:AAH/sendMessage"

LOG_FILENAME = "analytics.log"
logging.basicConfig(filename=LOG_FILENAME, level=logging.INFO, format='%(asctime)s %(message)s')
