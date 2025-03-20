import re

def validate_receipt(receipt):
    required_keys = {"retailer", "purchaseDate", "purchaseTime", "items", "total"}

    if not all(key in receipt for key in required_keys):
        return False

    if not isinstance(receipt["retailer"], str) or not re.match(r"^[\w\s\-&]+$", receipt["retailer"]):
        return False

    if not isinstance(receipt["purchaseDate"], str) or not re.match(r"^\d{4}-\d{2}-\d{2}$", receipt["purchaseDate"]):
        return False

    if not isinstance(receipt["purchaseTime"], str) or not re.match(r"^(?:[01]\d|2[0-3]):[0-5]\d$", receipt["purchaseTime"]):
        return False

    if not isinstance(receipt["total"], str) or not re.match(r"^\d+\.\d{2}$", receipt["total"]):
        return False

    if not isinstance(receipt["items"], list) or len(receipt["items"]) == 0:
        return False

    for item in receipt["items"]:
        if not isinstance(item, dict) or "shortDescription" not in item or "price" not in item:
            return False
        
        if not isinstance(item["shortDescription"], str) or not re.match(r"^[\w\s\-\&]+$", item["shortDescription"]):
            return False

        if not isinstance(item["price"], str) or not re.match(r"^\d+\.\d{2}$", item["price"]):
            return False

    return True
