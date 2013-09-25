"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""
from checkio.signals import ON_CONNECT
from checkio import api
from checkio.referees.io import CheckiOReferee
from checkio.referees import cover_codes
from checkio.referees import checkers



class CheckiOClassReferee(CheckiOReferee):

    def test_current_step(self):
        self.current_test = self.get_current_test()

        api.execute_function(
            func="exec",
            input_data=self.current_test["input"],
            callback=self.check_current_test,
            errback=self.fail_cur_step)

    # def get_current_env_name(self):
    #     return self.categories_names[self.current_category_index]
    #
    # def get_current_test(self):
    #     return self.tests[self.current_category][self.current_test_index]
    #
    # def check_current_test(self, data):
    #     user_result = data['result']
    #
    #     check_result = self.check_user_answer(user_result)
    #     self.current_test["result"], self.current_test["result_addon"] = check_result
    #
    #     api.request_write_ext(self.current_test)
    #
    #     if not self.current_test["result"]:
    #         return api.fail(self.current_step, self.get_current_test_fullname())
    #
    #     if self.next_step():
    #         self.test_current_step()
    #     else:
    #         if self.next_env():
    #             self.restart_env()
    #         else:
    #             api.success()
    #
    # def check_user_answer(self, result):
    #     if self.checker:
    #         return self.checker(self.current_test["answer"], result)
    #     else:
    #         return self.current_test["answer"] == result, None
    #
    # def next_step(self):
    #     self.current_step += 1
    #     self.current_test_index += 1
    #     return self.current_test_index < len(self.tests[self.current_category])
    #
    # def next_env(self):
    #     self.current_category_index += 1
    #     self.current_test_index = 0
    #     return self.current_category_index < len(self.categories_names)
    #
    # def restart_env(self):
    #     self.restarting_env = True
    #     api.kill_runner('req')
    #
    # def process_req_ended(self, data):
    #     if self.restarting_env:
    #         self.restarting_env = False
    #         self.start_env()
    #     else:
    #         api.fail(self.current_step, self.get_current_test_fullname())
    #
    # def fail_cur_step(self, data):
    #     api.fail(self.current_step, self.get_current_test_fullname())
    #
    # def get_current_test_fullname(self):
    #     return "Category: {0}. Test {1} from {2}".format(
    #         self.current_category,
    #         self.current_test_index + 1,
    #         len(self.tests[self.current_category]))



