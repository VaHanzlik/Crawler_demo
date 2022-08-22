from datetime import datetime
import time
import logging

from crawler_src.worker.extractor import Crawler_bot
from crawler_src.helpers.arg_parser import create_parser 
from crawler_src.helpers.log import setup_logging



def run(args= None):
    
    if args is None:
        parser = create_parser()
        args = parser.parse_args()
    
    setup_logging(filename=args.log_filename, debug = args.debug) ## init root logger
    logger = logging.getLogger(__name__) ## module logger

    try:
        logger.info("running crawler.py as main")
        logger.info("Initializing new crawler")
        Worker_bot = Crawler_bot(in_url =args.input_addr, max_depth = args.depth)
        logger.info("Start of crawling.")
        Worker_bot.crawl()
        logger.info("End of crawling.")
        
        logger.info("Start of saving results.")
        Worker_bot.dump_data(args.output_name)
        logger.info("End of saving results.")
    except KeyboardInterrupt as e:
        logger.info("Program aborted by user")
    except Exception as e:
        logger.info(e)

if __name__ == '__main__':
        run()
    
