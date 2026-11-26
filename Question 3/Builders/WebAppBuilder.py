from Builders.AppBuilder import AppBuilder
from Products.WebCustomer import WebCustomer

class WebAppBuilder(AppBuilder):

    def __init__(self) -> None:
        self._customer = WebCustomer()

    def _validate(self, customer: WebCustomer) -> None:
        required = {
            "firstName": customer.firstName,
            "middleName": customer.middleName,
            "lastName": customer.lastName,
            "primaryEmail": customer.primaryEmail,
            "secondaryEmail": customer.secondaryEmail,
            "primaryMobile": customer.primaryMobileNumber,
            "secondaryMobile": customer.secondaryMobileNumber,
        }

        #missing = required. Iterate over required, if anything is None, it remains in missing.
        missing = [
            name for name, val in required.items()
            if not val or not val.strip()
        ]

        if missing:
            raise ValueError(
                f"WebCustomer is missing required field(s): {', '.join(missing)}"
            )

    @property
    def result(self) -> WebCustomer:
        customer = self._customer
        self._customer = WebCustomer()
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