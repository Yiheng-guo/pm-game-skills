# ebitengine-game: acceptance scenarios

1. The world package tests pass and a clean checkout builds for the intended target. Record the fixture, action, expected result and observed result.
2. Focus loss, resize and browser audio activation are exercised in the actual build. Record the fixture, action, expected result and observed result.
3. Update owns simulation and Draw cannot mutate authoritative state. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
