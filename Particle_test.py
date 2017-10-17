from pytest import mark

from hypothesis import given
from hypothesis.strategies import floats

sensible_floats = floats(min_value=0.1, max_value=1e3, allow_nan=False,
                         allow_infinity=False)
FLOATS = sensible_floats

from Particle import Particle


@given(FLOATS, FLOATS, FLOATS, FLOATS, FLOATS)
def test_Particle_constructor_should_set_basic_attributes(r, x, y, vx, vy):
    p = Particle(r, (x, y), (vx, vy))
    assert p.r == r
    assert p.x == x
    assert p.y == y
    assert p.vx == vx
    assert p.vy == vy


@given(FLOATS, FLOATS, FLOATS, FLOATS, FLOATS)
def test_Particle_should_move_with_constant_velocity(r, x, y, vx, vy):
    p = Particle(r, (x, y), (vx, vy))
    dt = 10
    p.move(dt)
    assert p.r == r
    assert p.x == x + dt * p.vx
    assert p.y == y + dt * p.vy
    assert p.vx == vx
    assert p.vy == vy


bounce_data = ("""comment
                  r
                  x     y     vx     vy                  
                  xmin xmax ymin ymax
                  x_new y_new vx_new vy_new""".split(),
               (
                   ('no bounce',
                    20,
                    130, 140, 100, 200,
                    0, 500, 0, 600,
                    130, 140, 100, 200),
                   ('left boundary far',
                    30,
                    50, 500, -10, 40,
                    100, 900, 200, 800,
                    210, 500, 10, 40),
                   ('right boundary far',
                    35,
                    900, 500, 50, 60,
                    200, 800, 100, 700,
                    630, 500, -50, 60),
                   ('bottom boundary far',
                    12,
                    700, 0, 30, 50,
                    0, 1000, 100, 1000,
                    700, 224, 30, -50),
                   ('top boundary far',
                    13,
                    421, 1023, 500, 600,
                    0, 1000, 100, 1000,
                    421, 951, 500, -600),
                   ('left boundary near',
                    50,
                    149, 300, -10, 10,
                    100, 500, 100, 500,
                    151, 300, 10, 10),
                   ('right boundary near',
                    50,
                    451, 300, 10, 10,
                    100, 500, 100, 500,
                    449, 300, -10, 10),
                   ('bottom boundary near',
                    50,
                    300, 149, 10, -10,
                    100, 500, 100, 500,
                    300, 151, 10, 10),
                   ('top boundary near',
                    50,
                    300, 451, 10, 10,
                    100, 500, 100, 500,
                    300, 449, 10, -10)))


@mark.parametrize(*bounce_data)
def test_Particle_bounce_should_be_elastic(
        comment,
        r,
        x, y, vx, vy,
        xmin, xmax, ymin, ymax,
        x_new, y_new, vx_new, vy_new
):
    p = Particle(r, (x, y), (vx, vy))
    p.bounce((xmin, xmax, ymin, ymax))
    assert p.x == x_new
    assert p.y == y_new
    assert p.vx == vx_new
    assert p.vy == vy_new


@mark.parametrize(*bounce_data)
def test_bounce_should_leave_Particle_within_boundaries(
        comment,
        r, x, y, vx, vy,
        xmin, xmax, ymin, ymax,
        x_new, y_new, vx_new, vy_new
):
    p = Particle(r, (x, y), (vx, vy))
    p.bounce((xmin, xmax, ymin, ymax))
    assert p.x + p.r <= xmax
    assert p.x - p.r >= xmin
    assert p.y + p.r <= ymax
    assert p.y - p.r >= ymin
