# unity-build-pipeline: acceptance scenarios

1. A clean player build launches the intended first scene. Record the fixture, action, expected result and observed result.
2. Missing scene inclusion, platform modules and stripped types are checked. Record the fixture, action, expected result and observed result.
3. Addressable or remote content failures show recovery instead of a blank screen. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
