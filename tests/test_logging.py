from unittest import TestCase
import log_manager


class TestLogging(TestCase):
    def test_get_strategy_list(self):
        lm=log_manager.Logging('log')
        c=lm.get_strategy_list()
        self.assertGreater(len(c),0)
