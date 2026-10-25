# godot-nodes-scenes: acceptance scenarios

1. Two instances of a reusable scene operate independently. Record the fixture, action, expected result and observed result.
2. Removing a child or missing a resource produces a clear recoverable error. Record the fixture, action, expected result and observed result.
3. Reloading the scene does not accumulate autoload state or signals. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
