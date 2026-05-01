import logging

logger = logging.getLogger(__name__)

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Request: {symbol} {side} {order_type} {quantity}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        else:
            raise ValueError("Invalid order type")

        logger.info(f"Response: {order}")
        return order
        
        if not order:
            raise Exception("Empty response from Binance API")

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise