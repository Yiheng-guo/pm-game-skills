# unity-scriptableobjects: acceptance scenarios

1. Two actors share configuration but maintain independent current stats. Record the fixture, action, expected result and observed result.
2. Repeated play mode and domain-reload settings cannot persist unintended mutations. Record the fixture, action, expected result and observed result.
3. Event-channel subscriptions are removed on object disable. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
