import logging

def get_logger(name: str):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler("extraction.log"),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger(name)