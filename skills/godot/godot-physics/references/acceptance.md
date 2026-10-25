# godot-physics: acceptance scenarios

1. The intended collision pair is confirmed in a runnable 2D or 3D scene. Record the fixture, action, expected result and observed result.
2. Layer/mask mismatch, fast motion and overlapping spawn are covered. Record the fixture, action, expected result and observed result.
3. The actual physics backend and fixed-step settings are recorded. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
