import os
import time
import redis
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

redis_host = os.environ.get('REDIS_HOST', 'redis')
redis_port = int(os.environ.get('REDIS_PORT', 6379))

def get_redis():
    while True:
        try:
            r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)
            r.ping()
            logger.info(f"Connected to Redis at {redis_host}:{redis_port}")
            return r
        except Exception as e:
            logger.warning(f"Redis not ready, retrying... {e}")
            time.sleep(2)

def process_jobs(r):
    logger.info("Worker started - processing jobs...")
    counter = 0
    while True:
        counter += 1
        job = f"job-{counter}"
        r.lpush("processed_jobs", job)
        logger.info(f"Processed: {job}")
        time.sleep(5)

if __name__ == '__main__':
    r = get_redis()
    process_jobs(r)