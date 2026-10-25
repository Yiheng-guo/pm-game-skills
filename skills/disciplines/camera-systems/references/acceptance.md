# camera-systems: acceptance scenarios

1. The player and next actionable hazard remain in frame at level edges. Record the fixture, action, expected result and observed result.
2. Teleport, respawn and extreme aspect ratios do not expose outside bounds. Record the fixture, action, expected result and observed result.
3. Camera shake never changes collision or targeting coordinates. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
