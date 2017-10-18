# A context manager for timing code. Note: do not use this for serious
# timings: the overhead will be too large when the timed duration is
# very short. For serious timings use the timeit module.

from pytest import mark
from time import sleep

from timer import timer

@mark.parametrize('seconds_to_sleep', range(1,4))
def test_timer_should_report_approximately_correct_times(seconds_to_sleep):
    with timer() as t:
        sleep(seconds_to_sleep)
    sleep(1)
    assert abs(t.time - seconds_to_sleep) < 0.01
