from utilities.logGeneration import LogGen


class ScratchPad:
    logger = LogGen.log()

    def log_check(self):
        print("this is method in class scratchPad")
        self.logger.info("printing log message from another module")


if __name__ == '__main__':
    sp = ScratchPad()
    sp.log_check()

