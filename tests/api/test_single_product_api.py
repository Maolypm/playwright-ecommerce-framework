def test_get_single_product(api_context):
    
    response = api_context.get("/products/1")
    assert response.status == 200

    body = response.json()

    assert body["id"] == 1
    assert "title" in body