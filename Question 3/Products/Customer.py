class Customer:

    def __init__(self) -> None:
        self.firstName: str | None = None
        self.middleName: str | None = None
        self.lastName: str | None = None
        self.primaryEmail: str | None = None
        self.secondaryEmail: str | None = None
        self.primaryMobileNumber: str | None = None
        self.secondaryMobileNumber: str | None = None