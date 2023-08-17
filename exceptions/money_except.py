class MoneyException(ValueError):
    def __init__(self, value: str = "variable name") -> None:
        super().__init__(f"error: the value '{value}' is not valid for money.")
