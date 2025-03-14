import json
import os
import random

from payos import PaymentData, ItemData, PayOS
from flask import Flask, render_template, jsonify, request

payOS = PayOS(client_id= os.environ.get('PAYOS_CLIENT_ID'), api_key=os.environ.get('PAYOS_API_KEY'), checksum_key=os.environ.get('PAYOS_CHECKSUM_KEY'))

app = Flask(__name__, static_folder='public',
            static_url_path='', template_folder='public')

@app.route('/create-payment-link', methods=['POST'])
def create_payment():
        domain = "http://127.0.0.1:5000"
        try:
            paymentData = PaymentData(orderCode=random.randint(1000,99999), amount=10000, description="trung hieu",\
                                      cancelUrl= f"{domain}/cancel.html", returnUrl= f"{domain}/success.html")

            payosCreateResponse = payOS.createPaymentLink(paymentData)
            print(payosCreateResponse.to_json())

            return jsonify(payosCreateResponse.to_json())
        except Exception as e:
            print(e)
            return jsonify(error=str(e)), 403
    

if __name__ == '__main__':
    app.run(port=4242)

    