# unreal-enhanced-input: acceptance scenarios

1. The possessed local player receives move, look and action bindings. Record the fixture, action, expected result and observed result.
2. Possession changes and context priority conflicts do not duplicate or swallow input. Record the fixture, action, expected result and observed result.
3. Mapping contexts are removed from the matching player subsystem on teardown. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
