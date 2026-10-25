# pygame-core: acceptance scenarios

1. An isolated environment opens the game, processes events and exits cleanly. Record the fixture, action, expected result and observed result.
2. Quit during play, resize and missing mixer support do not freeze the process. Record the fixture, action, expected result and observed result.
3. Elapsed time drives movement and surfaces are reused where practical. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
