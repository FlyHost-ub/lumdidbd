"""
All the things that should be easibly changable
"""

from . import strings

# bot
BOT_TOKENS = {
    "main": "6225207433:AAE8WwWM8KL55P1cZMN1aN4J2XNZ2FjJUYM",
    "test": "5736701653:AAFYFyHvDrA83JEVA-O_u5HX1fS1-fqR0C8"
}
BOT_TOKEN = BOT_TOKENS["test"]

# cryptopay
CRYPTOPAY_TOKENS = {
    "mainnet": "x",
    "testnet": "x"
}
CRYPTOPAY_TOKEN = CRYPTOPAY_TOKENS["testnet"]
CRYPTOPAY_TESTNET = CRYPTOPAY_TOKEN == CRYPTOPAY_TOKENS["testnet"]
CRYPTOPAY_EXPIRE = 3600  # crypto bot payments expire time in seconds

# other
IP = "1111.1111.1111.1111"
FORBIDDEN_PORTS = [1]
ADMINS = [2]
PRICE = 666  # in RUB
CARD = "12345678"
USERBOTS = {
    "hikka": strings.HIKKA,
    "netfoll": strings.NETFOLL
}
