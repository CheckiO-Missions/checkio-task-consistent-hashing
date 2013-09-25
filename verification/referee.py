from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from checkio.referees import checkers

from tests import TESTS

class CheckiOClassReferee(CheckiOReferee):

    def test_current_step(self):
        self.current_test = self.get_current_test()

        api.execute_function(
            func="exec",
            input_data=self.current_test["input"],
            callback=self.check_current_test,
            errback=self.fail_cur_step)


api.add_listener(
    ON_CONNECT,
    CheckiOClassReferee(tests=TESTS).on_ready)