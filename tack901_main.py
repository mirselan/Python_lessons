# Создайте программу для игры в ""Крестики-нолики""
# при помощи виртуального окружения и PIP.
#####################################################


# Функция main
from task901_controller import controller
from task901_constants import FIELD


def main():
    controller(FIELD)


main()