# unity-input-system: acceptance scenarios

1. Gameplay and UI action maps receive the intended actions. Record the fixture, action, expected result and observed result.
2. Device switching, rebinding conflicts and lost focus cannot leave held actions. Record the fixture, action, expected result and observed result.
3. The active input backend and UI input module agree. Record the fixture, action, expected result and observed result.

Run the smallest relevant scenario in the real engine/browser, then the neighboring lifecycle path.
For an existing project, compare before/after using the same fixture. A document validator or mocked API does not verify the engine behavior. Mark unavailable runtimes as untested; include the command or manual steps another developer can run.
