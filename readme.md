# Micro servicio de authenticacion 
_Microservicio de authenticacion desarrollado en django y postgreSQL_

## EndPoints 📋

### Registrar usuario
_post _

```
.../user/
```
_dirver user_
```
{
    "username":  "" ,
    "password":  "",
    "email": "",
    "typeAccount":  "D",
        "car": {
            "carRegistrationNumber": "",
            "cityRegistration": "",
            "color": "",
            "brand": "",
            "model": "",
            "description": "",
            "equipament": ""
            }
}
```

_user (Passenger)_
```
{
    "username":  "" ,
    "password":  "",
    "email": "",
    "typeAccount":  "P"
}
```