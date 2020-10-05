from entities.models import Merchant

# Merchant Helper Functions


def create_merchants(number_of_merchants):

    for _ in range(number_of_merchants):
        Merchant.objects.create(name="Merchant", phone=123123)

    merchants = Merchant.objects.all()
    return merchants


def create_merchant(merchant_details):
    print(merchant_details, " \n\n are merchant details \n\n")
    new_merchant = Merchant(name=merchant_details["name"],
                            email=merchant_details["email"],
                            phone=merchant_details["phone"])
    new_merchant.save()
    return new_merchant
