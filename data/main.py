from publisher import published

data = {
    "id": 1,
    "title": "Gaseosa Coca Cola 3 L",
    "image": "https://jumbo.vtexassets.com/arquivos/ids/582628/Bebida-Coca-Cola-original-3-L.jpg?v=638004170224770000",
    "price": "15.00",
}

published(method="updated", body=data)
