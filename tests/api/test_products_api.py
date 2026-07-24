def test_get_products(api_context):
    
    response = api_context.get("/products")
    assert response.status == 200

    body = response.json()

    assert "products" in body

    assert len(body["products"]) > 0