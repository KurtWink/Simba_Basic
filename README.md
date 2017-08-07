### Simba_Basic
Simba_Basic is an early stage prototype for an industrial control system simulation and design tool.

Users are able to create their own Python Modules which are used to preform custom operations on a set of jQuery data that is loaded into the tool.
The modified jQuery data is then given a tag classifed by the operations preformed, and can be either saved to a local file system or be made as a HTTP POST request as a payload.

### Current Support
The default url assembly is configured primarly for the ease of GridState use. However, data can be GET/POST from any url location as long as the host follows the same REST structure.

Currently the only supported response type is JSON. Local filesystem imports/exports are expected to be handled in text form or any process that can be correctly loaded by the JSON python module.

Modules are expected to be revisions of the current mod template. Any number of classes can be merged into one .py module as long as it follows the description conditions. Any multithreading, streaming, addtional modules(numpy) will require the user to have those packages installed. 
Please keep this in mind when using shared mods. 

### Known Issues/Bugs
Be mindful of whitespace. Due to the flexiablity of user choices, whitespace and special line characters (\n) are not parsed out of the entry fields. 
If you are having issues with pulling from a service, I would suggest clearing your entries completely and verifying your information.

Do not open multiple Hosted Service/Export Windows. The tk GUI framework does not have good support for additonal top level windows, and as such the rootwork is currently unstable. 
Implementing a singleton pattern could fix this issue for the addtional frames.

The current socket/streaming is not using a verifying SSL handshake. I've looked into this and have tried all of the newest certificates, however I have no control over custom certs. 
Thus, for ease of not having to handle everyone's own certs, it is disabled. 
