# godot-3d-essentials: acceptance scenarios

1. An exported scene has a current camera, visible geometry and readable lighting. Record the fixture, action, expected result and observed result.
2. Near-plane clipping, aspect changes and missing environment do not yield a blank screen. Record the fixture, action, expected result and observed result.
3. Local/global transforms remain correct after reparenting. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
