# level-design: acceptance scenarios

1. A complete start-to-goal route is reachable using the actual movement metrics. Record the fixture, action, expected result and observed result.
2. The player can recover from detours or is told how to restart after a softlock. Record the fixture, action, expected result and observed result.
3. A later level introduces a new decision rather than only repeating a larger layout. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
