from Builders.AppBuilder import AppBuilder
from Products.MobileCustomer import MobileCustomer

class MobileAppBuilder(AppBuilder):

    def __init__(self) -> None:
        self._customer = MobileCustomer()

    def _validate(self, customer: MobileCustomer) -> None:
        required = {
            "firstName": customer.firstName,
            "lastName": customer.lastName,
            "primaryEmail": customer.primaryEmail,
            "primaryMobile": customer.primaryMobileNumber,
        }

        #missing = required. Iterate over required, if anything is None, it remains in missing.
        missing = [
            name for name, val in required.items()
            if not val or not val.strip()
        ]

        if missing:
            raise ValueError(
                f"MobileCustomer is missing required field(s): {', '.join(missing)}"
            )

    @property
    def result(self) -> MobileCustomer:
        customer = self._customer
        self._customer = MobileCustomer()
        self._validate(customer)
        return customer

    def setFirstName(self, value: str) -> None:
        self._customer.firstName = value

    def setMiddleName(self, value: str) -> None:
        self._customer.middleName = value

    def setLastName(self, value: str) -> None:
        self._customer.lastName = value

    def setPrimaryEmail(self, value: str) -> None:
        self._customer.primaryEmail = value

    def setSecondaryEmail(self, value: str) -> None:
        self._customer.secondaryEmail = value

    def setPrimaryPhone(self, value: str) -> None:
        self._customer.primaryMobileNumber = value

    def setSecondaryPhone(self, value: str) -> None:
        self._customer.secondaryMobileNumber = value