# godot-2d-movement: acceptance scenarios

1. The CharacterBody2D walks, jumps and lands in a runnable scene. Record the fixture, action, expected result and observed result.
2. Slopes, ceilings and floor edges do not reset jump state incorrectly. Record the fixture, action, expected result and observed result.
3. Velocity is applied in the physics callback with matching Godot-version APIs. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
