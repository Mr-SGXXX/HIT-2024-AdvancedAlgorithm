import logging
import os
import shutil

from generate_data import generate_data 
from greedy import greedy
from LP import LP
from check_rst import check_rst

DATA_DIR = "./lab3/results"

def get_logger(log_dir, description):
    formatter = logging.Formatter('[%(asctime)s]: %(message)s')

    # Create logger object
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)

    # Set file handler
    shutil.rmtree(log_dir, ignore_errors=True)
    os.makedirs(log_dir)
    log_dir = os.path.join(log_dir, f"{description}.log")
    handler = logging.FileHandler(log_dir)
    handler.setLevel(logging.INFO)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def main():
    logger = get_logger(DATA_DIR, 'rst')
    
    data_num_list = [100, 1000, 5000]
    for data_num in data_num_list:
        x, F = generate_data(data_num)
        greedy_C = greedy(F, x)
        LP_C = LP(F, x)
        logger.info(f'Data num: {data_num} ')
        logger.info(f'Greedy C size: {len(greedy_C)}')
        logger.info(f'LP C size: {len(LP_C)}')
        logger.info(f'Greedy C: {greedy_C}')
        logger.info(f'LP C: {LP_C}')
        logger.info(f"Greedy check result: {check_rst(x, F, greedy_C)}")
        logger.info(f"LP check result: {check_rst(x, F, LP_C)}")

        

if __name__ == '__main__':
    main()