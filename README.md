# Schema Registry API Wrapper

This Python module provides a wrapper for the Schema Registry API. This makes it easier to interact with the API in a Pythonic way, rather than dealing directly with HTTP requests.

## Installation

1. Clone this repository to your local machine using `git clone <repo-link>`.
2. Navigate to the cloned directory.
3. Install required Python packages using `pip install -r requirements.txt`.

## Usage

1. Import the `SchemaRegistryAPI` class from the module.

```python
from schema_registry_api import SchemaRegistryAPI
```

1. Instantiate an object of the class.

```python
api = SchemaRegistryAPI()
```

Use the methods provided by the class to interact with the API.

### API Methods

Refer to the [Schema Registry API documentation](https://docs.confluent.io/platform/current/schema-registry/develop/api.html#schemas) for more information on the API methods.

### Error Handling

Each method will return a Python Exception in case of an error. Error code 40403 indicates that the schema was not found and 50001 indicates an error in the backend datastore.

## License

This project is licensed under the terms of the MIT license.

## Contact

For more information, questions, or feedback, please feel free to reach out to me at `alexbryant710@gmail.com`.
