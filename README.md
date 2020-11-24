# dd-mobile-bridge

JSON description of mobile bridges used by cross-platform or hybrid mobile frameworks (React Native, Xamarin, …)

## Bridge API

### Interfaces

#### Datadog

The entry point to initialize Datadog's features.

- `initialize(configuration: DatadogConfiguration)`

    Initializes Datadog's features.

    - `configuration`: The configuration to use.

#### DdLogs

The entry point to use Datadog's Logs feature.

- `debug(message: string, context: map)`

    Send a log with level debug.

    - `message`: The message to send.
    - `context`: The additional context to send.

- `info(message: string, context: map)`

    Send a log with level info.

    - `message`: The message to send.
    - `context`: The additional context to send.

- `warn(message: string, context: map)`

    Send a log with level warn.

    - `message`: The message to send.
    - `context`: The additional context to send.

- `error(message: string, context: map)`

    Send a log with level error.

    - `message`: The message to send.
    - `context`: The additional context to send.

#### DdTrace

The entry point to use Datadog's Trace feature.

- `startSpan(operation: string, timestamp: long, context: map)`

    Start a span, and returns a unique identifier for the span.

    - `operation`: The operation name of the span.
    - `timestamp`: The timestamp when the operation started.
    - `context`: The additional context to send.

- `finishSpan(spanId: string, timestamp: long, context: map)`

    Finish a started span.

    - `spanId`: The unique identifier of the span.
    - `timestamp`: The timestamp when the operation stopped.
    - `context`: The additional context to send.

#### DdRum

The entry point to use Datadog's RUM feature.

- `startView(key: string, name: string, timestamp: long, context: map)`

    Start tracking a RUM View.

    - `key`: The view unique key identifier.
    - `name`: The view name.
    - `timestamp`: The timestamp when the view started.
    - `context`: The additional context to send.

- `stopView(key: string, timestamp: long, context: map)`

    Stop tracking a RUM View.

    - `key`: The view unique key identifier.
    - `timestamp`: The timestamp when the view stopped.
    - `context`: The additional context to send.

- `startAction(type: string, name: string, timestamp: long, context: map)`

    Start tracking a RUM Action.

    - `type`: The action type (tap, scroll, swipe, click, custom).
    - `name`: The action name.
    - `timestamp`: The timestamp when the action started.
    - `context`: The additional context to send.

- `stopAction(timestamp: long, context: map)`

    Stop tracking the ongoing RUM Action.

    - `timestamp`: The timestamp when the action stopped.
    - `context`: The additional context to send.

- `addAction(type: string, name: string, timestamp: long, context: map)`

    Add a RUM Action.

    - `type`: The action type (tap, scroll, swipe, click, custom).
    - `name`: The action name.
    - `timestamp`: The timestamp when the action occured.
    - `context`: The additional context to send.

- `startResource(key: string, method: string, url: string, timestamp: long, context: map)`

    Start tracking a RUM Resource.

    - `key`: The resource unique key identifier.
    - `method`: The resource method (GET, POST, …).
    - `url`: The resource url.
    - `timestamp`: The timestamp when the resource started.
    - `context`: The additional context to send.

- `stopResource(key: string, statusCode: long, kind: string, timestamp: long, context: map)`

    Stop tracking a RUM Resource.

    - `key`: The resource unique key identifier.
    - `statusCode`: The resource status code.
    - `kind`: The resource's kind (xhr, document, image, css, font, …).
    - `timestamp`: The timestamp when the resource stopped.
    - `context`: The additional context to send.

- `addError(message: string, source: string, stacktrace: string, timestamp: long, context: map)`

    Add a RUM Error.

    - `message`: The error message.
    - `source`: The error source (network, source, console, logger, …).
    - `stacktrace`: The error stacktrace.
    - `timestamp`: The timestamp when the error occured.
    - `context`: The additional context to send.

### Data structures

#### DatadogConfiguration

A configuration object to initialize Datadog's features.

- `clientToken` (string): A valid Datadog client token.
- `env` (string): The application’s environment, for example: prod, pre-prod, staging, etc.
- `applicationId` (string): The RUM application ID.

