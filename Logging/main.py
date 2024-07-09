import requests as rq
import logging
sites = ['https://www.youtube.com/', 'https://instagram.com', 'https://wikipedia.org', 'https://yahoo.com',
         'https://yandex.ru', 'https://whatsapp.com', 'https://twitter.com', 'https://amazon.com', 'https://tiktok.com',
         'https://www.ozon.ru']
#Log level INFO
suc_logger = logging.getLogger('success_response')
suc_logger.setLevel(logging.INFO)
fh = logging.FileHandler('success_responses.log')
fh.setFormatter(logging.Formatter('%(levelname)s | %(message)s'))
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(levelname)s | %(message)s'))
suc_logger.addHandler(fh)
suc_logger.addHandler(ch)
#Log level WARNING
bad_logger = logging.getLogger('bad_response')
bad_logger.setLevel(logging.WARNING)
fh = logging.FileHandler('bad_responses.log')
fh.setFormatter(logging.Formatter('%(levelname)s | %(message)s'))
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(levelname)s | %(message)s'))
bad_logger.addHandler(fh)
bad_logger.addHandler(ch)
#Log level ERROR
block_logger = logging.getLogger('block_response')
block_logger.setLevel(logging.INFO)
fh = logging.FileHandler('blocked_responses.log')
fh.setFormatter(logging.Formatter('%(levelname)s | %(message)s'))
ch = logging.StreamHandler()
ch.setFormatter(logging.Formatter('%(levelname)s | %(message)s'))
block_logger.addHandler(fh)
block_logger.addHandler(ch)
for site in sites:
    try:
        response = rq.get(site, timeout=3)
        site_code = response.status_code
        if site_code == 200:
            suc_logger.info(f"'{site}', response - {site_code}")
        elif site_code != 200:
            bad_logger.warning(f"'{site}', response - {site_code}")
    except rq.RequestException:
        block_logger.error(f"'{site}', response - NO CONNECTION")