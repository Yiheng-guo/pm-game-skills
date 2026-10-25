# steam-publish: acceptance scenarios

1. The exact depot build installs and launches from a test branch. Record the fixture, action, expected result and observed result.
2. Wrong launch executable, missing depots and platform prerequisites are checked. Record the fixture, action, expected result and observed result.
3. Store visibility, paid onboarding and release actions require existing authorization. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
