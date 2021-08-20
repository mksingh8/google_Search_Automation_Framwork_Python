from utilities.logGeneration import LogGen


class TestC001:
    logger = LogGen.log()

    def test_log_check_pytest(self):
        print("this is pytest class")
        self.logger.info("logging entries from another module by running pytest")
