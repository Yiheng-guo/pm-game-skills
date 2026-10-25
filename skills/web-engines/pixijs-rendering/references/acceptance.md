# pixijs-rendering: acceptance scenarios

1. Async application initialization renders sprites at the intended resolution. Record the fixture, action, expected result and observed result.
2. Missing textures, resize and renderer fallback are handled. Record the fixture, action, expected result and observed result.
3. Removed containers release owned resources without destroying shared textures. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
