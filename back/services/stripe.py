import os
import stripe
import requests

def create_checkout(reference, name, unit_price, quantity, confirmation_secret):
    """
        Create Stripe checkout
        Documentation: https://docs.stripe.com/checkout/quickstart?client=react&lang=python
    """
    
    stripe.api_key = "rk_test_51RhVfI2aoAWLbEQqd67veWGXyEfUURYFN5oILPW0kVLEMbAHX7jg7581yVSeggp04xRaDFE68JmDZVIDZCNSWE0X008r1rAkXU"
    origin_host = os.getenv('APP_ORIGIN_HOST')
    return stripe.checkout.Session.create(
        mode='payment',
        success_url=f"{origin_host}/booking/{reference}?checkout_confirmation_secret={confirmation_secret}",
        cancel_url=origin_host,
        line_items=[
            {
                'quantity': quantity,
                'price_data': {
                    'currency': 'EUR',
                    'unit_amount': round(unit_price * 100),
                    'product_data': {
                        'name': name,
                    },
                },
            },
        ],
    )

def get_checkout_lines(checkout_session_id):
    url = f"https://api.stripe.com/v1/checkout/sessions/{checkout_session_id}/line_items"

    session = requests.Session()
    session.auth = ("rk_test_51RhVfI2aoAWLbEQqd67veWGXyEfUURYFN5oILPW0kVLEMbAHX7jg7581yVSeggp04xRaDFE68JmDZVIDZCNSWE0X008r1rAkXU", "")
    return session.get(url).json()["data"]
