# shader-programming: acceptance scenarios

1. The intended effect compiles on the target renderer and preserves readable silhouettes. Record the fixture, action, expected result and observed result.
2. Missing textures, extreme uniform values and low-end precision fail predictably. Record the fixture, action, expected result and observed result.
3. Material instances do not unintentionally mutate every object sharing the resource. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
