# phaser-core: acceptance scenarios

1. The pinned Phaser major starts, loads assets and switches scenes. Record the fixture, action, expected result and observed result.
2. Failed asset loads, resize and focus loss produce usable states. Record the fixture, action, expected result and observed result.
3. Scene shutdown releases input handlers, timers and external listeners. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
