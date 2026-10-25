# godot-audio: acceptance scenarios

1. Streams use the intended buses and saved mute/volume settings. Record the fixture, action, expected result and observed result.
2. Missing stream, unavailable device and browser activation do not block startup. Record the fixture, action, expected result and observed result.
3. Scene reload does not layer duplicate music players. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
