import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY

def create_payment_intent(amount, currency='usd'):
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
    )
    return intent