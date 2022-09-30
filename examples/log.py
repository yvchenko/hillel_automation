import logging

logging.basicConfig(filename='data.log',
                    level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger('Our logger')

file_name = 'example.txt'

try:
    with open(file_name, 'r') as f:
        logger.info(f'file {file_name} successfully opened')
        data = f.read()
        if data:
            logger.debug(f'data from {file_name}: {data}')
        else:
            logger.debug(f'data was not retrieved from {file_name}')
except FileNotFoundError:
    logger.error(f'file with the name {file_name} does not exist.')
    with open(file_name, 'w') as f:
        logger.warning(f'file {file_name} was created.')
    data = 'inside file'

print(data)

# logger.debug('Debug')
# logger.info('Info')
# logger.warning('Warning')
# logger.error('Error')
# logger.critical('Critical')