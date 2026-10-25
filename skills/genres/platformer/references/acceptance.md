# platformer: acceptance scenarios

1. The actual controller completes a representative jump, landing and goal route. Record the fixture, action, expected result and observed result.
2. Buffered jump, ledge departure, ceiling contact and respawn avoid stuck states. Record the fixture, action, expected result and observed result.
3. Camera, animation and particles cannot change collision truth. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
