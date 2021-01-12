# dd-mobile-bridge

> JSON description of mobile bridges used by cross-platform or hybrid mobile frameworks (React Native, Xamarin, …)

This repository is used to provide a unified API to interact with all of Datadog's Mobile SDKs.

## API Definition

The API definition is provided in the [mobile-bridge-api.json](mobile-bridge-api.json) file. 
You can also see the definition in a more readable format in [API_REFERENCE.md](API_REFERENCE.md).

## Code generation

To ensure that all SDKs do follow the same API definition, python scripts are used to generate the relevant source code 
in all the dependants project. Code generation is triggered automatically whenever a new Tag is created on this 
repository. 

## Contributing

Pull requests are welcome. First, open an issue to discuss what you would like to change. For more information, read the [Contributing Guide](CONTRIBUTING.md).

## License

[Apache License, v2.0](LICENSE)
