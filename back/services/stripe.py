import os
import re
from urllib.parse import quote

import stripe
import requests

def create_checkout(reference, name, unit_price, quantity, confirmation_secret):
    """
        Create Stripe checkout
        Documentation: https://docs.stripe.com/checkout/quickstart?client=react&lang=python
    """
    
    stripe.api_key = os.getenv('STRIPE_API_KEY')
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

CHECKOUT_SESSION_ID = re.compile(r'^cs_(?:test|live)_[A-Za-z0-9]+$')

def get_checkout_lines(checkout_session_id):
    """
        Get the line items of a Stripe checkout session
    """

    # On vérifie le format de l'ID avant de l'utiliser dans l'URL,
    # sinon on peut viser une autre route de l'API Stripe (ex : ../../customers#)
    if not isinstance(checkout_session_id, str) or not CHECKOUT_SESSION_ID.fullmatch(checkout_session_id):
        raise ValueError("Invalid checkout session ID")

    # Normalement inutile avec la regex, mais on encode quand même par sécurité
    url = f"https://api.stripe.com/v1/checkout/sessions/{quote(checkout_session_id, safe='')}/line_items"

    session = requests.Session()
    session.auth = (os.getenv('STRIPE_API_KEY'), "")
    response = session.get(url, timeout=10)
    response.raise_for_status()
    return response.json()["data"]
