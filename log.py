import logging
import timeit

# logging.basicConfig(level=logging.INFO, filename="test.log",filemode="w",
#                     format="%(asctime)s %(levelname)s %(message)s")

logger2 = logging.getLogger(__name__)
logger2.setLevel(logging.INFO)
handler2 = logging.FileHandler(f"{__name__}.log", mode='w')
formatter2 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
handler2.setFormatter(formatter2)
logger2.addHandler(handler2)
logger2.info(f"Testing the custom logger for module {__name__}...")

def test_division(x,y):
        z = sorted(x)
        if z == y:
            logger2.info(f"Sort {x} successful with {y}.")
        else:
            logger2.info(f"Sort {x} not successful with {y}.")

def test_time(x,y):
    time_def = timeit.timeit(lambda:x(y), globals=globals(), number=1)
    logger2.info(f"Function execution time {x.__name__}: {time_def}")