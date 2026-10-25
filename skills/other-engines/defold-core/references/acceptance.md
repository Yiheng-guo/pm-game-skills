# defold-core: acceptance scenarios

1. Bob builds the project and the main collection reaches a controllable scene. Record the fixture, action, expected result and observed result.
2. Missing hashed ids, proxy load failure and repeated input focus are handled. Record the fixture, action, expected result and observed result.
3. Collection unload releases listeners and never routes messages to deleted objects. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
