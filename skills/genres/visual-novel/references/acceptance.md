# visual-novel: acceptance scenarios

1. A short route reaches an ending through at least one consequential choice. Record the fixture, action, expected result and observed result.
2. Skipping, auto mode and rapid clicks cannot select an unintended choice. Record the fixture, action, expected result and observed result.
3. Backlog and save/load preserve speaker, line position and flags. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
