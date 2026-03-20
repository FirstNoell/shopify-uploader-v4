def upload_product(product):
    """
    Simplified Shopify upload function (demo only)
    """
    print(f"Uploading: {product['title']}")

    # Placeholder logic only
    # Full implementation is private

    return {
        "status": "success",
        "product": product["title"]
    }


if __name__ == "__main__":
    sample_product = {
        "title": "Sample Product"
    }

    result = upload_product(sample_product)
    print(result)
