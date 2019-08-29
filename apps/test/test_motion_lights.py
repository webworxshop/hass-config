
import pytest
from appdaemontestframework import automation_fixture
from apps.motion_lights import MotionLight

@automation_fixture(MotionLight)
def motion_light(given_that):
    given_that.passed_arg("motion_sensor").is_set_to("binary_sensor.motion")
    given_that.passed_arg("light").is_set_to("light.test_light")
    given_that.passed_arg("timeout").is_set_to(120)

def test_working(given_that, motion_light, assert_that):
    assert(True)

