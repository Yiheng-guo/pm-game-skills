# unity-csharp-scripting: acceptance scenarios

1. The component compiles and its behavior works through enable/disable/reload. Record the fixture, action, expected result and observed result.
2. Missing serialized references and destroyed objects do not throw each frame. Record the fixture, action, expected result and observed result.
3. OnEnable subscriptions are paired with OnDisable cleanup. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
