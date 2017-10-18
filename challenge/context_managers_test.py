from pytest import mark

from context_managers1 import timer
from context_managers2 import redirected_std_streams

################################################################################
# The basic context manager exercise
################################################################################
# A context manager for timing code. Note: do not use this for serious
# timings: the overhead will be too large when the timed duration is
# very short. For serious timings use the timeit module.

           ############## Test ##############

from time import sleep

@mark.parametrize('seconds_to_sleep', range(1,4))
def test_timer_should_report_approximately_correct_times(seconds_to_sleep):
    with timer() as t:
        sleep(seconds_to_sleep)
    sleep(1)
    assert abs(t.time - seconds_to_sleep) < 0.01


################################################################################
# The challenge exercise for context managers
################################################################################
################################################################################
################################################################################
# A Context manager for temporarily redirecting stdout, stderr and stdin

           ############## Tests ##############

from io import StringIO
import sys

def test_stream_redirect_should_be_able_to_unpack_into_3_separate_values():
    """Checks that the as-target of the with statement can be unpacked
    into the 3 objects. These 3 objects should be the bindings of
    sys.stdout, sys.stderr and sys.stdin which are in effect within
    the with block."""
    stdout_text = 'stdout'
    stderr_text = 'stderr'
    stdin_text  = 'stdin\n'
    with redirected_std_streams(StringIO(), StringIO(), StringIO(stdin_text)) as (out, err, in_):
        print(stdout_text)
        print(stderr_text)
        assert input() == stdin_text[:-1]
    assert out.getvalue() == stdout_text + '\n'
    assert err.getvalue() == stderr_text + '\n'

def test_stream_redirect_attribute_names_should_be_out_err_in_():
    """Checks that the as-target of the with statement has three
    attributes, out, err and in_. These should be the bindings or
    sys.stdout, sys.stderr and sys.stdin which are in effect within
    the with block. """
    stdout_text = 'stdout'
    stderr_text = 'stderr'
    stdin_text  = 'stdin\n'
    with redirected_std_streams(StringIO(), StringIO(), StringIO(stdin_text)) as streams:
        print(stdout_text)
        print(stderr_text)
        assert input() == stdin_text[:-1]
    assert streams.out.getvalue() == stdout_text + '\n'
    assert streams.err.getvalue() == stderr_text + '\n'

def test_nested_stream_redirection_should_work():
    """Checks that two nested stream redirection context managers
    restore the intermediate and original bindings as expected."""
    print("0 before")
    with redirected_std_streams(StringIO()) as (out, err, in_):
        print("1 before")
        with redirected_std_streams(StringIO()) as streams:
            print("inside")
        print("1 after")
    print("0 after")

    assert out.getvalue() == "1 before\n1 after\n"
    assert streams.out.getvalue() == "inside\n"

def test_stream_redirection_should_reset_streams_when_exception_raised():
    """Checks that redirected streams are correctly restored even when
    an exception is raised in the with block."""
    with redirected_std_streams(StringIO()) as (outer, _, _):
        try:
            with redirected_std_streams(StringIO()) as (inner, _, _):
                print("inner")
                raise Exception
                print("never happens")
        except Exception:
            pass
        print("outer")
    assert inner.getvalue() == "inner\n"
    assert outer.getvalue() == "outer\n"

def test_should_be_able_to_redirect_just_one_stream_by_keyword_argument():
    """Checks that a single one of the 3 standard streams can be
    redirected with a keyword argument, leaving the other two alone."""
    with redirected_std_streams(StringIO(), StringIO(), StringIO('stdin before\nstdin after\n')) as (out1, err1, in1):
        print("stderr before", file=sys.stderr)
        with redirected_std_streams(stderr=StringIO()) as (out2, err2, in2):
            print("inner stderr", file=sys.stderr)
        print("stderr after", file=sys.stderr)
    assert out1 is out2
    assert in1  is in2
    assert err2 is not err1
    assert err1.getvalue() == "stderr before\nstderr after\n"
    assert err2.getvalue() == "inner stderr\n"
