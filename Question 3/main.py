#imagine this as a pseudo director class.

from Builders.AppBuilder import AppBuilder
from Builders.WebAppBuilder import WebAppBuilder
from Builders.MobileAppBuilder import MobileAppBuilder

def buildCustomer(builder: AppBuilder):
    builder.setFirstName("Alex")
    builder.setMiddleName("Jordan")
    builder.setLastName("Taylor")
    builder.setPrimaryEmail("alex@example.com")
    builder.setSecondaryEmail("alex.work@example.com")
    builder.setPrimaryPhone("555-0100")
    builder.setSecondaryPhone("555-0199")
    return builder.result


def buildSmallCustomer(builder: AppBuilder):
    builder.setFirstName("Tom")
    builder.setLastName("Thompson")
    builder.setPrimaryEmail("alex@example.com")
    builder.setPrimaryPhone("555-0100")
    return builder.result

webBuilder = WebAppBuilder()
webCustomer = buildCustomer(webBuilder)

mobileBuilder = MobileAppBuilder()
mobileCustomer = buildCustomer(mobileBuilder)

print("Web customer:", vars(webCustomer))
print("Mobile customer:", vars(mobileCustomer))

#should execute

mobileCustomer = buildSmallCustomer(mobileBuilder)
print("Small Mobile customer:", vars(mobileCustomer))

#should error

webCustomer = buildSmallCustomer(webBuilder)