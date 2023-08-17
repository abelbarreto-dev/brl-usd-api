class MoneyException(ValueError):
    def __init__(self, message: str = "ValueError") -> None:
        super().__init__(message)
