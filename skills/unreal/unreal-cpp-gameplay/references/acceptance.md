# unreal-cpp-gameplay: acceptance scenarios

1. The module builds and a packaged actor exercises the exposed gameplay API. Record the fixture, action, expected result and observed result.
2. Garbage-collected references, null actors and invalid server requests are handled. Record the fixture, action, expected result and observed result.
3. Reflected ownership and generated-header placement match Unreal's build rules. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
