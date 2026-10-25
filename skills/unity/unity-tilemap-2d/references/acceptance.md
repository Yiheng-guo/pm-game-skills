# unity-tilemap-2d: acceptance scenarios

1. Painted tiles render and collide in a runnable player scene. Record the fixture, action, expected result and observed result.
2. Negative coordinates, empty tiles and collider rebuild timing are tested. Record the fixture, action, expected result and observed result.
3. Palette assets and runtime map state have separate ownership. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
