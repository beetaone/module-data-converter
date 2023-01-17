# Data Converter

|           |                                                                        |
| --------- | ---------------------------------------------------------------------- |
| Name      | Data Converter                                                         |
| Version   | v1.0.0                                                                 |
| DockerHub | [data-converter](https://hub.docker.com/r/weevenetwork/data-converter) |
| Authors   | Ghassen Barbouchi                                                      |

***
## Table of Content

- [Data Converter](#data-converter)
  - [Table of Content](#table-of-content)
  - [Description](#description)
    - [Features](#features)
  - [Module Variables](#module-variables)
    - [Module Specific](#module-specific)
    - [Set by the weeve Agent on the edge-node](#set-by-the-weeve-agent-on-the-edge-node)
  - [Dependencies](#dependencies)
  - [Input](#input)
  - [Output](#output)
***

## Description

The function of this module is to convert the selected input of the previous module to another type. Available options are hex string, int, ieee754 float, text, and data can be converted from and to those types.
### Features

1. Detect the value to convert from the incoming JSON data.
2. Validate the selected from type.
3. Convert the detected value from selected input Type to selected out Type.
4. Forward the new converted JSON to the next module.
## Module Variables

### Module Specific

| Environment Variables | type   | Description                    |
| --------------------- | ------ | ------------------------------ |
| INPUT_KEY             | string | Input Key eg "Device.pc.price" |
| FROM_TYPE             | string | Input type                     |
| TO_TYPE               | string | Output type                    |

### Set by the weeve Agent on the edge-node

There are 5 module variables that are required by each module to correctly function within weeve ecosystem. In development, these variables can overridden for testing purposes. In production, these variables are set by weeve Agent.

| Environment Variables | type   | Description                                                                                          |
| --------------------- | ------ | ---------------------------------------------------------------------------------------------------- |
| MODULE_NAME           | string | Name of the module                                                                                   |
| MODULE_TYPE           | string | Type of the module (Input, Processing, Output)                                                       |
| LOG_LEVEL             | string | Allowed log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL. Refer to `logging` package documentation. |
| INGRESS_HOST          | string | Host to which data will be received                                                                  |
| INGRESS_PORT          | string | Port to which data will be received                                                                  |
| EGRESS_URLS           | string | HTTP ReST endpoint for the next module                                                               |

## Dependencies

The following are module dependencies:

* bottle
* requests

The following are developer dependencies:

* pytest
* flake8
* black

## Input

Input example:

```json
{
"manufacturer" : "weeve",
"device" :{
"SN" : "1232",
"newobj":{
      "a":12,
      "b":"0xFD"
},
"year" : 2021
}
}
```
## Output

output example in case the input key is : "device.newobj.b" , the fromType :"hex" and the toType :"int"

```json
{
"manufacturer" : "weeve",
"device" :{
"SN" : "1232",
"newobj":{
      "a":12,
      "b":253
},
"year" : 2021
}
}
```

