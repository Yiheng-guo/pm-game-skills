# godot-animation: acceptance scenarios

1. Requested state transitions play once with a stable return to idle. Record the fixture, action, expected result and observed result.
2. Interrupted tweens, freed targets and overlapping transitions do not leave a distorted pose. Record the fixture, action, expected result and observed result.
3. Animation method tracks cannot grant gameplay rewards twice. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
