## API Reference

<hr>

### App Home Pagess ( GET `/` )

#### RESPONSE

```json
{
	"merchants": "localhost:port/merchants/",
	"stores": "localhost:port/stores/",
	"items": "localhost:port/items/",
	"orders": "localhost:port/orders/"
}
```
<hr>

### Fetch List of Merchants ( GET `/merchants/` )

#### RESPONSE


```python
[
    {
     "pk": Integer,
    "name": String,
    "email": String,
    "phone": String,
    "created_at": String
    },
]
```

### Fetch Details of a Merchant ( GET `/merchants/<integer:merchant ID>/` )

#### RESPONSE

```python
{
     "pk": Integer,
    "name": String,
    "email": String,
    "phone": String,
    "created_at": String
}
```

### Fetch Items belonging to the Merchant ( GET `/merchants/<integer:merchant ID>/items/`)

#### RESPONSE

```python
[
    {
        "pk": Integer,
        "name": String,
        "merchant": Integer,
        "cost": String,
        "description": String,
        "created_at": String
    },
]
```

### Fetch Stores belonging to the Merchant ( GET `/merchants/<integer:merchant ID>/stores/`)

#### RESPONSE

```python
[
    {
        "pk": Integer,
        "name": String,
        "merchant": Integer,
        "address": String,
        "lon": String,
        "lat": String,
        "active": Boolean,
        "items": Array of Item IDs(Integers),
        "created_at": String
    },
]
```

### Fetch Orders belonging to the Merchant ( GET `/merchants/<integer:merchant ID>/orders/`)

#### RESPONSE

```python
[
    {
    "pk": Integer,
    "merchant": Integer,
    "store": Integer,
    "total_cost": String,
    "status": String,
    "items": Array of Item IDs(Integers),
    "created_at": String
    },
]
```

### Create a New Merchant ( POST `/merchants/` )

#### REQUEST

```python
{
    "name": String,
    "email": String, [Optional]
    "phone": String,
}
```

#### RESPONSE

```python
{   
    "pk" : String,
    "name": String,
    "email": String,
    "phone": String,
    "created_at": String
}
```

### Update a Particular Merchant ( PATCH `/merchants/<integer:merchant ID>` )

#### REQUEST

```python
{
    "name": String,
    "email": String, [Optional]
    "phone": String,
}
```

#### RESPONSE

```python
{   
    "pk" : String,
    "name": String,
    "email": String, 
    "phone": String,
    "created_at": String
}
```

<hr>

### Fetch List of Stores ( GET `/stores/` )

#### RESPONSE


```python
[
    {
     "pk": Integer,
        "name": String,
        "merchant": Integer,
        "address": String,
        "lon": String,
        "lat": String,
        "active": Boolean,
        "items": Array of Item IDs(Integers),
        "created_at": String
    },
]
```

### Fetch Details of a Store ( GET `/stores/<integer:store ID>/` )

#### RESPONSE

```python
{
     "pk": Integer,
        "name": String,
        "merchant": Integer,
        "address": String,
        "lon": String,
        "lat": String,
        "active": Boolean,
        "items": Array of Item IDs(Integers),
        "created_at": String
}
```

### Create a New Store ( POST `/stores/` )

#### REQUEST

```python

{
        "name": String,
        "merchant": Integer,
        "address": String, [Optional]
        "lon": String, [Optional]
        "lat": String, [Optional]
        "active": Boolean, [Optional]
        "items": Array of Item IDs(Integers),
}

```

#### RESPONSE

```python
{
        "pk": Integer,
        "name": String,
        "merchant": Integer,
        "address": String,
        "lon": String,
        "lat": String,
        "active": Boolean,
        "items": Array of Item IDs(Integers),
        "created_at": String
}

```


### Update a Particular Store ( PATCH `/stores/` )

#### REQUEST

```python

{
        "name": String,
        "merchant": Integer,
        "address": String, [Optional]
        "lon": String, [Optional]
        "lat": String, [Optional]
        "active": Boolean, [Optional]
        "items": Array of Item IDs(Integers),
}

```

#### RESPONSE

```python
{
        "pk": Integer,
        "name": String,
        "merchant": Integer,
        "address": String,
        "lon": String,
        "lat": String,
        "active": Boolean,
        "items": Array of Item IDs(Integers),
        "created_at": String
}

```

<hr>

### Fetch List of Items ( GET `/items/` )

#### RESPONSE


```python
[
     {
        "pk": Integer,
        "name": String,
        "merchant": Integer,
        "cost": String,
        "description": String,
        "created_at": String
    },
]
```

### Fetch Details of a Item ( GET `/items/<integer:item ID>/` )

#### RESPONSE

```python
{
     "pk": Integer,
    "name": String,
    "merchant": Integer,
    "cost": String,
    "description": String,
    "created_at": String
}
```

### Create a New Item ( POST `/items/` )

#### REQUEST


```python

{
        "name": String,
        "merchant": Integer,
        "cost": String,
        "description": String, [Optional]
}

```

#### RESPONSE


```python

{
        "pk": Integer,
        "name": String,
        "merchant": Integer,
        "cost": String,
        "description": String, 
        "created_at" : String
}

```

### Update a Particular Item ( PATCH `/items/<integer:item ID>/` )

#### REQUEST


```python

{
        "name": String,
        "merchant": Integer,
        "cost": String,
        "description": String, [Optional]
}

```

#### RESPONSE


```python

{
        "pk": Integer,
        "name": String,
        "merchant": Integer,
        "cost": String,
        "description": String, 
        "created_at" : String
}

```

<hr>

### Fetch List of Orders ( GET `/orders/` )

#### RESPONSE


```python
[
     {
        "pk": Integer,
        "merchant": Integer,
        "store": Integer,
        "total_cost": String,
        "status": String,
        "items": Array of Item IDs(Integers),
        "created_at": String
    },
]
```

### Fetch Details of a Order ( GET `/orders/<integer:order ID>/` )

#### RESPONSE

```python
{
    "pk": Integer,
    "merchant": Integer,
    "store": Integer,
    "total_cost": String,
    "status": String,
    "items": Array of Item IDs(Integers),
    "created_at": String
}
```

### Create a New Order ( POST `/orders/` )

#### REQUEST


```python

{
        "pk": Integer,
        "merchant": Integer,
        "store": Integer,
        "total_cost": String,
        "status": String, [Optional]
        "items": Array of Item IDs(Integers),
}

```

#### RESPONSE


```python

{
        "pk": Integer,
        "merchant": Integer,
        "store": Integer,
        "total_cost": String,
        "status": String, [Optional]
        "items": Array of Item IDs(Integers),
}

```

### Update a Particular Order ( PATCH `/orders/<integer:order ID>/` )

#### REQUEST


```python

{
        "pk": Integer,
        "merchant": Integer,
        "store": Integer,
        "total_cost": String,
        "status": String, [Optional]
        "items": Array of Item IDs(Integers),
}

```

#### RESPONSE


```python

{
        "pk": Integer,
        "merchant": Integer,
        "store": Integer,
        "total_cost": String,
        "status": String, [Optional]
        "items": Array of Item IDs(Integers),
}

```
