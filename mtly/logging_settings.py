import logging


lg = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s] %(module)20s:%(lineno)3d %(levelname)10s "
           f"->{' '*4}%(message)s"
)
