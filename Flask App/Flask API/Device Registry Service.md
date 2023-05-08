//https://www.youtube.com/watch?v=4T5Gnrmzjak&list=PLlj9BrHKq9WI4R30l_M_tdRMPF4AZ6dcs&index=2
# Device Registry Service

## Usage

All responses will have the form

```json
{
    "data": "Mixed type holding the content of the response",
    "message": "Description of what happened"
}
```

Subsequent response definitions will only detail the excepted value of the `data field`

### List all devices

**Definition**
`GET /devices`

**Response**

- `200 OK` on success

```json
[
    {
        "identifier": "floor-lamp",
        "name": "Floor Lamp",
        "device_type": "switch",
        "controller_gateway": "192.1.6.2"
    },
    {
        "identifier": "samsung-tv",
        "name": "Monitor",
        "device_type": "switch",
        "controller_gateway": "192.1.6.3"
    }
]
```
### Registering a new device

**Definition**

`POST /devices`

**Arguments**

- `"identifier":string` a globally unique identifier for this device
- `"name":string` a friendlt name for this device
- `"device_type":string` the type of the device as understood by the client
- `"controller_gateway":string` the IP address of the device's controller

IF a device with the given identifier already exists, the existing device will be overwritten

**Response**

- `201 Created` on success

```json
    {
        "identifier": "samsung-tv",
        "name": "Monitor",
        "device_type": "switch",
        "controller_gateway": "192.1.6.3"
    }
```

## Lookup device details

`GET /device/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `200 OK` on success

```json
{
        "identifier": "samsung-tv",
        "name": "Monitor",
        "device_type": "switch",
        "controller_gateway": "192.1.6.3"
}
```
## Delete a device

**Definition**

`DELETE /device/<identifier>`

**Response**

-`404 Not Found` if the device does not exist
-`204 No Content`