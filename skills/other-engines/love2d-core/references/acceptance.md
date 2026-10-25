# love2d-core: acceptance scenarios

1. The game starts with the declared LÖVE version and completes one gameplay loop. Record the fixture, action, expected result and observed result.
2. Large dt after focus loss and missing assets do not crash or jump simulation. Record the fixture, action, expected result and observed result.
3. Window restart and state transitions do not retain duplicate callbacks. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
