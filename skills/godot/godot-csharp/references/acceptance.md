# godot-csharp: acceptance scenarios

1. The declared .NET SDK builds scripts against the project's exact Godot version. Record the fixture, action, expected result and observed result.
2. Missing exported references fail with a useful message rather than a null crash. Record the fixture, action, expected result and observed result.
3. Signal subscriptions are removed before managed nodes are freed. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
