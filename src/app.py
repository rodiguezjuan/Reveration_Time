from utils.registro import config_log


def add_nums(num1: int, num2: int) -> int:
    """This method will be used to add two numbers

    :param num1: The first number
    :type num1: int
    :param num2: The second number
    :type num2: int
    :return: The sum of two numbers
    :rtype: int
    """

    answer = num1 + num2
    return answer


if __name__ == "__main__":
    logger = config_log()
    logger.info("Running project ...")
