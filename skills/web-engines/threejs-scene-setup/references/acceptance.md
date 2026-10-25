# threejs-scene-setup: acceptance scenarios

1. Scene, camera and renderer display correctly after startup and resize. Record the fixture, action, expected result and observed result.
2. WebGL unavailable, zero-size container and background resume fail gracefully. Record the fixture, action, expected result and observed result.
3. One animation loop owns rendering and teardown disposes controls and renderer. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
